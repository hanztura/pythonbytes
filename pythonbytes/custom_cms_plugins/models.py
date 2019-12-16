from django.db import models

from cms.models import CMSPlugin


class CodePluginModel(CMSPlugin):
    code = models.TextField()
    code_language = models.CharField(max_length=30, blank=True)

    def __str__(self):
        name = '{} - {}'.format(self.id, self.code_language)
        return name
