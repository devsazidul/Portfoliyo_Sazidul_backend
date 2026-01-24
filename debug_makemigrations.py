import os
import django
from django.conf import settings
from django.core.management import call_command
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print(f"Final host check: {settings.DATABASES['default']['CLIENT']['host'][:35]}...")

try:
    # We call with verbosity 3 to see the internal operations
    call_command('makemigrations', 'api', interactive=False, verbosity=3)
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
