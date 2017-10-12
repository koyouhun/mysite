# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Scenario(models.Model):
    """
    시나리오 정보
    """

    ######
    # Class 변수 선언
    ######
    INACTIVE, ACTIVE = False, True
    SCENARIO_STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active'))
    )

    FREE, MALE_ONLY, FEMALE_ONLY = None, True, False
    GENDER_CHOICES = (
        (FREE, _('Free')),
        (MALE_ONLY, _('Male Only')),
        (FEMALE_ONLY, _('Female Only'))
    )

    YES, NO = True, False
    ADULT_CHOICES = (
        (YES, _('Adult Only')),
        (NO, _('Free'))
    )

    master = models.CharField(
        _("Master Name"),
        max_length=64,
        null=True
    )

    name = models.CharField(
        _("Scenario Name"),
        max_length=128
    )

    adult_only = models.BooleanField(
        _("Adult Only"),
        choices=ADULT_CHOICES,
        default=NO
    )

    gender_only = models.NullBooleanField(
        _("Gender Only"),
        default=None,
        choices=GENDER_CHOICES
    )

    is_active = models.BooleanField(
        _("Is Active"),
        choices=SCENARIO_STATUS,
        default=ACTIVE
    )

    reg_date = models.DateTimeField(
        _("Reg Date"),
        auto_now_add=True
    )

    modify_date = models.DateTimeField(
        _("Modify Date"),
        auto_now=True
    )

    def __str__(self):
        return self.name

    def get_characters(self):
        return self.character.all()

    class Meta:
        verbose_name = _('Scenario')
        verbose_name_plural = _("Scenarios")
