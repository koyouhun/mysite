# -*- coding:utf-8 -*-

# Python Module

# Django Module
from django.contrib import admin

# Third Party Library

# Local Module
from mysite.apps.character.models import Character
from mysite.apps.player.models import Player
from mysite.apps.scenario.models import Scenario


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'scenario', 'player', 'status')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'gender', 'is_adult', 'email', 'reg_date', 'modify_date')


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'adult_only', 'gender_only', 'is_active')

