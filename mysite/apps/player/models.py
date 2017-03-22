# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Player(models.Model):
    """
    플레이어 정보
    """
    ######
    # Class 변수 선언
    ######
    MALE, FEMALE = True, False
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    YES, NO = True, False
    ADULT_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No'))
    )

    name = models.CharField(
        _("Player Name"),
        max_length=64
    )

    phone_number = models.CharField(
        _("Phone Number"),
        max_length=16
    )

    gender = models.BooleanField(
        _("Gender"),
        choices=GENDER_CHOICES,
        default=MALE
    )

    is_adult = models.BooleanField(
        _("Is Adult"),
        choices=ADULT_CHOICES,
        default=YES
    )

    email = models.EmailField(
        _("Email"),
        max_length=64
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

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _("Players")
