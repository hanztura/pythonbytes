from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page


class CodePluginModel(CMSPlugin):
    code = models.TextField()
    code_language = models.CharField(max_length=30, blank=True)

    def __str__(self):
        name = '{} - {}'.format(self.id, self.code_language)
        return name


class CardPlugin(CMSPlugin):
    TITLE_TAGS = (
        ('h1', 'h1'),
        ('h2', 'h2'),
        ('h3', 'h3'),
        ('h4', 'h4'),
        ('h5', 'h5'),
        ('h6', 'h6'),
        ('span', 'span'),
    )

    title = models.CharField(max_length=50)
    title_tag = models.CharField(
        max_length=10, blank=True, default='span', choices=TITLE_TAGS)
    body = models.TextField()
    main_internal_link = models.ForeignKey(
        Page,
        verbose_name=_('Main internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    main_internal_text = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.title


class SimpleSubscribePlugin(CMSPlugin):
    submit_url_name = models.CharField(max_length=100)
    has_name = models.BooleanField(default=False, blank=True)
    is_recaptcha_enabled = models.BooleanField(default=True)
