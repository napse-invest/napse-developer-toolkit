import os
from unittest import mock

import celery
from celery.app import trace
from celery.signals import setup_logging

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
app = celery.Celery("napse_dtk")


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Gestion des logs ------------------------------------------------------------------
# Remove the trace from celery logs
old_info = trace.info
trace.info = mock.Mock()


# Configure celery logging
@setup_logging.connect
def config_loggers(*args, **kwags):
    """Take settings.LOGGING as config for celery loggers (especially for `formatters`)."""
    from logging.config import dictConfig

    from django.conf import settings

    dictConfig(settings.LOGGING)


# Remove the strategy from celery logs
def strategy_log_free(*args, **kwargs):
    """Remove the strategy from celery logs."""
    kwargs["info"] = mock.Mock()
    return celery.worker.strategy.default(*args[1:], **kwargs)


# Basor for task to remove the strategy
class StrategyFreeTaskBase(celery.Task):
    """Base for task to remove the strategy from celery logs."""

    strategy = strategy_log_free


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
