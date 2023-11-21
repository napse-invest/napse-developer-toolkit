import os

from config.settings.base import ROOT_DIR, env
from config.settings.modules import *  # noqa: F403

# DOCKER
# ------------------------------------------------------------------------------
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# DJANGO
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa: F405

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
if os.environ.get("DB_ENGINE") == "POSTGRES":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
    }
elif os.environ.get("DB_ENGINE") == "SQLITE":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ROOT_DIR / "db" / "db.sqlite3",
        },
    }
else:
    if os.environ.get("DB_ENGINE"):
        error_msg = f"DB_ENGINE={os.environ.get('DB_ENGINE')} is not supported."
    else:
        error_msg = "DB_ENGINE environment variable is not set."
    raise ValueError(error_msg)

DATABASES["default"]["ATOMIC_REQUESTS"] = True

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: S104
CORS_ALLOWED_ORIGINS = [f"http://{host}:8888" for host in ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = [f"http://{host}:8888" for host in ALLOWED_HOSTS]
