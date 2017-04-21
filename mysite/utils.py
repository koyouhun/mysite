# -*- coding:utf-8 -*-

# Python Module
import csv

# Django Module
from django.apps import apps

# Third Party Library

# Local Module

# Inner Module

# Local Model
Character = apps.get_app_config('character').get_model('Character')
Scenario = apps.get_app_config('scenario').get_model('Scenario')


def add_characters(path):
    """
    add characters from csv to db
    :param path: csv file
    """
    _read_characters(path)


def add_scenarios(path):
    """
    add scenario from csv to db
    :param path: csv file
    """
    _read_scenarios(path)


def reset_characters(path):
    """
    reset characters database with csv
    :param path: csv file
    """
    Character.objects.all().delete()
    _read_characters(path)


def reset_scenarios(path):
    Scenario.objects.all().delete()
    _read_scenarios(path)


def extract_characters(path):
    _read_characters(path)


def extract_scenarios(path):
    _read_scenarios(path)


def _read_characters(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for data in reader:
            character = Character()
            character.name = data[0]
            character.scenario = Scenario.objects.get(name=data[1])
            character.save()


def _read_scenarios(path):
    with open(path, 'r') as csvfile:
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
