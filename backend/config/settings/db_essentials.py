import json
from time import sleep

import environ
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django_napse.core.settings import napse_settings
from utils import sync_file_with_s3


@receiver(post_migrate)
def sync_master_key_s3(sender, **kwargs):
    env = environ.Env()
    if "AWS_ACCESS_KEY_ID" not in env or "AWS_SECRET_ACCESS_KEY" not in env or "AWS_S3_BUCKET_URI" not in env:
        print("AWS credentials not found. Skipping sync_master_key_s3")
        return
    master_key_created = False
    counter = 0
    while not master_key_created:
        with open(napse_settings.NAPSE_SECRETS_FILE_PATH, "r") as f:
            data = json.load(f)
        if "master_key" in data:
            master_key_created = True
        counter += 1
        sleep(1)
        print(f"Waiting for master key to be created. {counter} seconds passed")
        if counter > 10:
            error_msg = "Master key was not created in 10 seconds"
            raise ValueError(error_msg)
    sync_file_with_s3(napse_settings.NAPSE_SECRETS_FILE_PATH, "napse-eb-bucket", "napse-secrets.json")
