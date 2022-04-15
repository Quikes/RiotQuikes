from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import IntegerField
from riot_api.models import SummonerSimpleDataSolo, SummonerSimpleDataFlex

# Create your models here.


class CustomUser(AbstractUser):
    riot_account_id = models.CharField(max_length=150, blank=True, null=True)
    riot_puuid = models.CharField(max_length=150, blank=True, null=True)
    riot_name = models.CharField(max_length=150, blank=True, null=True)
    riot_profileIconId = models.CharField(max_length=150, blank=True, null=True)
    riot_summonerLevel = models.PositiveIntegerField(
        null=True,
    )
    riot_summoner_id = models.CharField(max_length=150, blank=True, null=True)
    riot_revision_date = models.PositiveBigIntegerField(
        blank=True, null=True, default=0
    )

    user_data_solo = models.ForeignKey(
        SummonerSimpleDataSolo,
        related_name="user",
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
    user_data_flex = models.ForeignKey(
        SummonerSimpleDataFlex,
        related_name="user",
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
