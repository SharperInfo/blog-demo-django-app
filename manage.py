#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# pylint: disable=import-outside-toplevel

import os
import sys
from contextlib import suppress


def main():
    """Django's command-line utility for administrative tasks."""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_demo_django_app.settings")

    with suppress(ModuleNotFoundError):
        import dotenv  # pylint: disable=import-error

        dotenv.load_dotenv(verbose=True)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your"
            " PYTHONPATH environment variable? Did you forget to activate a virtual"
            " environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
