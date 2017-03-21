# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Character(models.Model):
    """
    캐릭터 정보
    """

    ######
    # Class 변수 선언
    ######
    EMPTY, BOOKED, PAID = range(0, 3)
    CHARACTER_STATUS = (
        (EMPTY, _('Empty')),
        (BOOKED, _('Booked')),
        (PAID, _('Paid'))
    )

    name = models.CharField(
        _("Character_Name"),
        max_length=128
    )

    scenario = models.ForeignKey(
        'scenario.Scenario',
        related_name='character',
        verbose_name=_('Scenario'),
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        'player.Player',
        related_name='character',
        verbose_name=_('Player'),
        blank=True,
        null=True
    )

    status = models.PositiveSmallIntegerField(
        _("Status of booking"),
        choices=CHARACTER_STATUS,
        default=EMPTY
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('scenario',)
        verbose_name = _('Character')
        verbose_name_plural = _("Characters")
