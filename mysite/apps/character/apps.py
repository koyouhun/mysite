from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CharacterConfig(AppConfig):
    name = 'mysite.apps.character'
    verbose_name = _('Character')
    verbose_name_plural = _('Characters')
