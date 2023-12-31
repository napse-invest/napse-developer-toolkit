#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        error_msg: tuple[str] = (
            "Couldn't import Django. Are you sure it's installed and ",
            "available on your PYTHONPATH environment variable? Did you ",
            "fo.octivate a virtual environment?",
        )
        raise ImportError("".join(error_msg)) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
