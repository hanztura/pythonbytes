import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    message = models.TextField()
    email_address = models.EmailField()
    name = models.CharField(max_length=50)
    admin_notified = models.BooleanField(default=False, blank=True)
