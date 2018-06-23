#!/usr/bin/env python
import os
import sys

#if __name__ == "__main__":
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
#    try:
#        from django.core.management import execute_from_command_line
#    except ImportError as exc:
#        raise ImportError(
#            "Couldn't import Django. Are you sure it's installed and "
#            "available on your PYTHONPATH environment variable? Did you "
#            "forget to activate a virtual environment?"
#        ) from exc
#    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

    import django
    django.setup()

    # Override default port for `runserver` command
    from django.core.management.commands.runserver import Command as runserver
    try:
        runserver.default_port = process.env.PORT
    except:
        runserver.default_port = "8080"
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
