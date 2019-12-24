from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CodePluginModel, CardPlugin, SimpleSubscribePlugin
from newsletter.forms import SubscriberModelForm


@plugin_pool.register_plugin
class CodePluginPublisher(CMSPluginBase):
    model = CodePluginModel
    module = 'Custom'
    name = 'Code'
    text_enabled = True
    render_template = 'custom_cms_plugins/code_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class CardPluginPublisher(CMSPluginBase):
    model = CardPlugin
    module = 'Custom'
    name = 'Card'
    render_template = 'custom_cms_plugins/card_plugin.html'

    def render(self, context, instance, placeholder):
        instance = instance
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class SimpleSubscribePublisher(CMSPluginBase):
    module = 'Custom'
    name = 'Simple Subscriber'
    render_template = 'custom_cms_plugins/simple_subscriber_plugin.html'

    def render(self, context, instance, placeholder):
        instance = instance
        context.update({
            'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY,
        })
        return context


@plugin_pool.register_plugin
class SimpleContactFormPublisher(CMSPluginBase):
    module = 'Custom'
    name = 'Simple Contact Form'
    render_template = 'custom_cms_plugins/simple_contact_form.html'

    def render(self, context, instance, placeholder):
        instance = instance
        context.update({
            'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY,
        })
        return context
