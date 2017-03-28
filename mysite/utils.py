# -*- coding:utf-8 -*-

import unicodecsv as csv

from mysite.apps.character.models import Character
from mysite.apps.scenario.models import Scenario


def _read_characters(path):
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for data in reader:
            character = Character()
            character.name = data[0]
            character.scenario = Scenario.objects.get(name=data[1])
            character.save()


def _read_scenarios(path):
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for data in reader:
            scenario = Scenario()
            scenario.name = data[0]

            if data[1] == 'YES':
                scenario.adult_only = Scenario.ADULT_CHOICES['YES']
            else:
                scenario.adult_only = Scenario.ADULT_CHOICES['NO']

            if data[2] == 'MALE_ONLY':
                scenario.gender_only = Scenario.GENDER_CHOICES['MALE_ONLY']
            elif data[2] == 'FEMALE_ONLY':
                scenario.gender_only = Scenario.GENDER_CHOICES['FEMALE_ONLY']
            else:
                scenario.gender_only = Scenario.GENDER_CHOICES['FREE']

            scenario.save()


def add_characters(path):
    Character.objects.all().delete()
    _read_characters(path)


def add_scenarios(path):
    Scenario.objects.all().delete()
    _read_scenarios(path)


def reset_characters(path):
    Character.objects.all().delete()
    _read_characters(path)


def reset_scenarios(path):
    Scenario.objects.all().delete()
    _read_scenarios(path)
