#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    print("DJANGO_SETTINGS_MODULE: ", os.environ.get("DJANGO_SETTINGS_MODULE"))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        error_msg: tuple[str] = (
            "Couldn't import Django. Are you sure it's installed and ",
            "available on your PYTHONPATH environment variable? Did you ",
            "forget to activate a virtual environment?",
        )
        raise ImportError("".join(error_msg)) from exc
    execute_from_command_line(sys.argv)
    print("DJANGO_SETTINGS_MODULE: ", os.envirn.get("DJANGO_SETTINGS_MODULE"))


if __name__ == "__main__":
    main()
