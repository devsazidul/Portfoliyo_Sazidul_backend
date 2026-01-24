import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

User = get_user_model()
count = User.objects.count()
print(f"Total Users: {count}")
for u in User.objects.all():
    print(f"Username: {u.username}, Is Superuser: {u.is_superuser}")
