# -*- coding:utf-8 -*-


from .models import Player

from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'phone_number',
            'gender',
            'is_adult',
            'email',
            'reg_date',
            'modify_date',
        )
