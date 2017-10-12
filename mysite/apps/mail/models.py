from django.db import models


class Mail(models.Model):
    player_name = models.CharField(max_length=64)
    scenario_name = models.CharField(max_length=128)
    character_name = models.CharField(max_length=128)
    player_reg_date = models.DateTimeField()
    player_email = models.EmailField(max_length=64)
    player_phone_number = models.CharField(max_length=32, null=True)
