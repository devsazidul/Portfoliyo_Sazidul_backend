import os
import django
from django.conf import settings
from dotenv import load_dotenv

# Force load .env here just in case
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print(f"DATABASE HOST IN SCRIPT: {settings.DATABASES['default']['CLIENT']['host'][:30]}...")

from django.core.management import call_command
import sys

try:
    # Use -v 3 for maximum verbosity to see why it's timing out or hitting localhost
    call_command('makemigrations', 'api', interactive=False, verbosity=3)
except Exception as e:
    print(f"FAILED: {e}", file=sys.stderr)
