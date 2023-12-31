from config.settings.base import *  # noqa: F403
from config.settings.base import ROOT_DIR, env
from config.settings.modules import *  # noqa: F403

# Use merged .envs
env.read_env(str(ROOT_DIR / ".env"))


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "utils.sqlite3_with_busy_timeout.SqliteWithBusyTimeout",
        "NAME": ROOT_DIR / "db" / "db.sqlite3",
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
