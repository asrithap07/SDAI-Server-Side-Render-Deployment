import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ['DJANGO_SUPERUSER_USERNAME']
        email = os.environ['DJANGO_SUPERUSER_EMAIL']
        password = os.environ['DJANGO_SUPERUSER_PASSWORD']

        if not password:
            self.stdout.write(self.style.ERROR('Superuser password not set. Use DJANGO_SUPERUSER_PASSWORD environment variable.'))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))