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


def delete_selected(modeladmin, request, queryset):
    for player in queryset:
        character = Character.objects.get(player=player)
        character.status = Character.EMPTY
        character.save()
        player.delete()
delete_selected.short_description = "삭제 및 캐릭터 상태 변경"


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'gender', 'is_adult', 'email', 'reg_date', 'modify_date')
    actions = [delete_selected]

@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'adult_only', 'gender_only', 'is_active')
