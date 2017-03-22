# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scenario', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Character_Name')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Empty'), (1, 'Booked'), (2, 'Paid')], default=0, verbose_name='Status of booking')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character', to='player.Player', verbose_name='Player')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='scenario.Scenario', verbose_name='Scenario')),
            ],
            options={
                'verbose_name': 'Character',
                'verbose_name_plural': 'Characters',
                'ordering': ('scenario',),
            },
        ),
    ]
