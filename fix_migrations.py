import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command

try:
    print("Attempting makemigrations...")
    call_command('makemigrations', 'api', interactive=False)
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
