from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    name = 'apps.core'
    verbose_name = _('core')

    def ready(self):
        import apps.core.signals
