from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_text_ckeditor.cms_plugins import TextPlugin

from .models import Tutorial


@plugin_pool.register_plugin
class TutorialPluginPublisher(TextPlugin):
    model = Tutorial
    module = 'Tutorial'
    name = 'Tutorial plugin'
