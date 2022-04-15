from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class SummonerSimpleDataSolo(models.Model):
    tier = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    leaguePoints = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    veteran = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    fresh_blood = models.BooleanField(default=False)
    hot_streak = models.BooleanField(default=False)


class SummonerSimpleDataFlex(models.Model):
    tier = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    leaguePoints = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    veteran = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    fresh_blood = models.BooleanField(default=False)
    hot_streak = models.BooleanField(default=False)
