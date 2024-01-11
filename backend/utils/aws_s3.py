import json
from datetime import datetime

import boto3
import environ
from django.utils import timezone


def sync_file_with_s3(path: str, bucket_name: str, key: str):
    env = environ.Env()
    if "AWS_ACCESS_KEY_ID" not in env or "AWS_SECRET_ACCESS_KEY" not in env or "AWS_S3_BUCKET_URI" not in env:
        error_msg = "AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY or AWS_S3_BUCKET_URI is not set in .env file"
        raise ValueError(error_msg)

    s3 = boto3.client("s3", aws_access_key_id=env.get_value("AWS_ACCESS_KEY_ID"), aws_secret_access_key=env.get_value("AWS_SECRET_ACCESS_KEY"))
    with open(path, "r") as f:
        data = json.load(f)
        data["last_updated"] = str(datetime.now(tz=timezone.get_current_timezone()))
    with open(path, "w") as f:
        json.dump(data, f)
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
    print(f"Successfully synced {path} with S3 bucket {bucket_name} with key {key}")


def pull_file_from_s3(path: str, bucket_name: str, key: str):
    env = environ.Env()
    if "AWS_ACCESS_KEY_ID" not in env or "AWS_SECRET_ACCESS_KEY" not in env or "AWS_S3_BUCKET_URI" not in env:
        error_msg = "AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY or AWS_S3_BUCKET_URI is not set in .env file"
        raise ValueError(error_msg)

    s3 = boto3.client("s3", aws_access_key_id=env.get_value("AWS_ACCESS_KEY_ID"), aws_secret_access_key=env.get_value("AWS_SECRET_ACCESS_KEY"))
    s3.download_file(bucket_name, key, path)
    with open(path, "r") as f:
        data = json.load(f)
        data["last_updated"] = str(datetime.now(tz=timezone.get_current_timezone()))
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"Successfully pulled {path} from S3 bucket {bucket_name} with key {key}")
