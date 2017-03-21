# -*- coding:utf-8 -*-


from .models import Character

from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'scenario',
            'player',
            'status'
        )
