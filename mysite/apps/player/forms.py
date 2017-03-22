from django import forms
from django.utils.translation import ugettext_lazy as _

from mysite.apps.scenario.models import Scenario
from mysite.apps.character.models import Character
from .models import Player


class RegistForm(forms.Form):

    scenario = forms.ModelChoiceField(
        queryset=Scenario.objects.filter(is_active=Scenario.ACTIVE),
        empty_label="",
    )

    character = forms.ModelChoiceField(
        queryset=Character.objects.all(),
        empty_label="",
    )

    player_name = forms.CharField(max_length=64)
    player_phone_number = forms.CharField(max_length=16)
    player_gender = forms.ChoiceField(choices=Player.GENDER_CHOICES)
    player_adult = forms.ChoiceField(choices=Player.ADULT_CHOICES)
    player_email = forms.EmailField(max_length=64)

    agree_read_all = forms.BooleanField()
    agree_no_problem = forms.BooleanField()
    agree_face = forms.BooleanField()