"""Base settings to build other settings files upon."""
import logging
import sys
from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR / "custom"

# Setup env
env = environ.Env(
    DEBUG=(bool, False),
    IS_LOCAL=(bool, False),
)
DEBUG = env.bool("DJANGO_DEBUG", False)
IS_LOCAL = env.bool("IS_LOCAL", False)
SECRET_KEY = env("DJANGO_SECRET_KEY")


# TIME ZONE
# ------------------------------------------------------------------------------
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "CET"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# URLS
# ------------------------------------------------------------------------------
BASE_URL = "http://127.0.0.1:8000/"
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# Tests
# ------------------------------------------------------------------------------
IS_IN_TEST = False
if len(sys.argv) > 1 and sys.argv[1] == "test":
    logging.disable(logging.CRITICAL)
    IS_IN_TEST = True

# Health check
HEALTHCHECK_CELERY_TIMEOUT = 10

# Hosts
# ALLOWED_HOSTS = ["django"]

NAPSE_SECRETS_FILE_PATH = ROOT_DIR / "secrets.json"
NAPSE_ENV_FILE_PATH = ROOT_DIR / ".env"
NAPSE_EXCHANGE_CONFIGS = {
    "BINANCE": {
        "description": "Binance exchange. More info: https://www.binance.com/en",
    },
}
