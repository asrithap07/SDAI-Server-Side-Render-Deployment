import os
import uuid
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def scramble_uploaded_filename(instance, filename):
    '''
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)
    return os.path.join('images', new_filename)
    '''

    extension = filename.split(".")[-1]
    random_string = get_random_string(length=12)
    new_filename = f"{random_string}.{extension}"
    return os.path.join('images', new_filename)

class UploadAlert(models.Model):
    #creating the id
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
    user_ID = models.ForeignKey(Token, on_delete=models.CASCADE)
    alert_receiver = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)