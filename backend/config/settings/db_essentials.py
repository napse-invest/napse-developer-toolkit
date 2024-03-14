import json
from contextlib import suppress
from datetime import datetime, timedelta
from time import sleep

import environ
from botocore.exceptions import ClientError
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils import timezone
from django_napse.core.settings import napse_settings
from utils import sync_file_with_s3
from utils.aws_s3 import pull_file_from_s3


def needs_to_sync():
    with open(napse_settings.NAPSE_SECRETS_FILE_PATH, "r") as f:
        data = json.load(f)
        if data.get("last_updated", None) is None or datetime.now(tz=timezone.get_current_timezone()) - datetime.strptime(
            data["last_updated"],
            "%Y-%m-%d %H:%M:%S.%f%z",
        ) > timedelta(minutes=1):
            return True
    return False


@receiver(post_migrate)
def sync_master_key_s3(sender, **kwargs):
    env = environ.Env()
    if "AWS_ACCESS_KEY_ID" not in env or "AWS_SECRET_ACCESS_KEY" not in env or "AWS_S3_BUCKET_URI" not in env:
        print("AWS credentials not found. Skipping sync_master_key_s3")
        return
    bucket_name = env("AWS_S3_BUCKET_URI").split("s3://")[1].split("/")[0]
    if needs_to_sync():
        with suppress(ClientError):
            pull_file_from_s3(
                napse_settings.NAPSE_SECRETS_FILE_PATH,
                bucket_name,
                "napse-secrets.json",
            )

    master_key_created = False
    counter = 0
    while not master_key_created:
        with open(napse_settings.NAPSE_SECRETS_FILE_PATH, "r") as f:
            data = json.load(f)
        if "master_key" in data:
            master_key_created = True
            break
        counter += 1
        sleep(1)
        print(f"Waiting for master key to be created. {counter} seconds passed")
        if counter > 10:
            error_msg = "Master key was not created in 10 seconds"
            raise ValueError(error_msg)

    if needs_to_sync():
        sync_file_with_s3(napse_settings.NAPSE_SECRETS_FILE_PATH, bucket_name, "napse-secrets.json")
