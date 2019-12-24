from django import template
from django.conf import settings


register = template.Library()


@register.tag
def google_analytics():
    return settings.GOOGLE_ANALYTICS_PROPERTY_ID
