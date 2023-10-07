from config.settings.base import ROOT_DIR, env
from config.settings.modules import *  # noqa: F403

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "django"]

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
DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.environ.get("POSTGRES_DB"),
    #     "USER": os.environ.get("POSTGRES_USER"),
    #     "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    #     "HOST": os.environ.get("POSTGRES_HOST"),
    #     "PORT": os.environ.get("POSTGRES_PORT"),
    # },
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "db" / "db.sqlite3",
    },
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "nw.django"]  # noqa: S104
CORS_ALLOWED_ORIGINS = [f"http://{host}:8888" for host in ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = [f"http://{host}:8888" for host in ALLOWED_HOSTS]
