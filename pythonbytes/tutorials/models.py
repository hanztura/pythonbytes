from django.db import models

from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_text_ckeditor.models import AbstractText


class Tutorial(AbstractText):
    tutorial_title = models.CharField(max_length=200)

    def __str__(self):
        return self.tutorial_title
