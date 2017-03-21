from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ScenarioConfig(AppConfig):
    name = 'mysite.apps.scenario'
    verbose_name = _('Scenario')
    verbose_name_plural = _('Scenarios')
