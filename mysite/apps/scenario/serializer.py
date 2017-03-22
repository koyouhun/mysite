# -*- coding:utf-8 -*-

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