# -*- coding:utf-8 -*-

from mysite.apps.character.models import Character
from mysite.apps.player.models import Player
from .models import Scenario

from rest_framework import serializers


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = (
            'id',
            'name',
            'adult_only',
            'gender_only',
            'is_active',
        )


class PlayerInfo(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'name',
            'is_adult',
        )


class ScenarioDetailSerializer(serializers.ModelSerializer):
    player_info = PlayerInfo(source='player')

    class Meta:
        model = Character
        fields = (
            'name',
            'player_info',
            'status',
        )
        depth = 2