from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CodePluginModel, CardPlugin


@plugin_pool.register_plugin
class CodePluginPublisher(CMSPluginBase):
    model = CodePluginModel
    module = 'Custom'
    name = 'Code Plugin'
    text_enabled = True
    render_template = 'custom_cms_plugins/code_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class CardPluginPublisher(CMSPluginBase):
    model = CardPlugin
    module = 'Custom'
    name = 'Card Plugin'
    render_template = 'custom_cms_plugins/card_plugin.html'

    def render(self, context, instance, placeholder):
        instance = instance
        context.update({'instance': instance})
        return context
