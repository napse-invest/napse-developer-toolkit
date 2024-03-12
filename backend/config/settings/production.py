from config.settings.base import *  # noqa: F403
from config.settings.base import ROOT_DIR, env
from config.settings.modules import *  # noqa: F403
from django.db.backends.signals import connection_created
from django.dispatch import receiver

# Use merged .envs
env.read_env(str(ROOT_DIR / ".env"))

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "db" / "db.sqlite3",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ALLOWED_HOSTS = ["django", env("NAPSE_API_DOMAIN"), "localhost"]
print("ALLOWED_HOSTS", ALLOWED_HOSTS)


@receiver(connection_created)
def set_busy_timeout(sender, connection, **kwargs):
    if connection.vendor == "sqlite":
        cursor = connection.cursor()
        cursor.execute("PRAGMA busy_timeout = 5000;")


connection_created.connect(set_busy_timeout)

CORS_ALLOWED_ORIGINS = [f"http://{host} " for host in ALLOWED_HOSTS] + ["http://localhost:8888", "app://."]
CSRF_TRUSTED_ORIGINS = [f"http://{host} " for host in ALLOWED_HOSTS] + ["http://localhost:8888", "app://."]
