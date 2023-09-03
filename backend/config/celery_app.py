import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
from django_napse.core.celery_app import celery_app
