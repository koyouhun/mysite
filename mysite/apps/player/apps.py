from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PlayerConfig(AppConfig):
    name = 'mysite.apps.player'
    verbose_name = _('Player')
    verbose_name_plural = _('Players')
