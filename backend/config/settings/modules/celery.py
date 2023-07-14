import os

from config.settings.base import *  # noqa
from config.settings.base import env

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-timezone
    timezone = TIME_ZONE
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_backend
result_backend = CELERY_BROKER_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-accept_content
accept_content = ["json"]
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_serializer
task_serializer = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_serializer
result_serializer = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# Periodic task
beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"
# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# ACCOUNT_ADAPTER = "napsedjango._users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
# ACCOUNT_FORMS = {"signup": "napsedjango._users.forms.UserSignupForm" }
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# SOCIALACCOUNT_ADAPTER = "napsedjango._users.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
# SOCIALACCOUNT_FORMS = {"signup": "napsedjango._users.forms.UserSocialSignupForm"}

CELERY_WORKER_MAX_MEMORY_PER_CHILD = 200_000  # 200 MB
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
CELERY_WORKER_CONCURRENCY = 4
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
