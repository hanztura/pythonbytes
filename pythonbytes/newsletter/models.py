import random
import secrets
import uuid

from django.db import models

from django_extensions.db.models import ActivatorModel, TimeStampedModel
from djangocms_text_ckeditor.fields import HTMLField


class Newsletter(TimeStampedModel, ActivatorModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=50)
    body = HTMLField()
    is_delivered = models.BooleanField(default=False, blank=True)

    class Meta:
        abstract = False

    def __str__(self):
        return self.subject


class Subscriber(TimeStampedModel, ActivatorModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    email_address = models.EmailField()
    unsubscribe_key = models.CharField(
        max_length=50,
        default=secrets.token_urlsafe(20),
        editable=False)

    class Meta:
        abstract = False

    def save(self, *args, **kwargs):
        if not self.pk:
            # create a random subscriber key
            key_length = random.randint(20, 50)
            kwargs['unsubscribe_key'] = secrets.token_urlsafe(key_length)

        return super().save(*args, **kwargs)

    @property
    def possible_name(self):
        name = self.name

        if not name:
            # if no name, return the local part of email
            name = self.email_address.split('@')[0]

        return name

    def __str__(self):
        return self.email_address


class Delivery(TimeStampedModel):
    newsletter = models.ForeignKey(
        Newsletter,
        on_delete=models.PROTECT,
        related_name='subscribers')
    subscriber = models.ForeignKey(
        Subscriber,
        on_delete=models.PROTECT,
        related_name='newsletters')
    is_success = models.BooleanField(blank=True, default=False)

    class Meta:
        abstract = False
