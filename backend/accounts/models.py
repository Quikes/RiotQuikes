from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.forms import IntegerField

# Create your models here.

class CustomUser(AbstractUser):
    riot_account_id = models.CharField(max_length=150,blank=True)
    riot_puuid = models.CharField(max_length=150,blank=True)
    riot_name = models.CharField(max_length=150,blank=True)
    riot_profileIconId = models.CharField(max_length=150,blank=True)
    riot_summonerLevel = models.PositiveIntegerField(null=True)
    riot_summoner_id = models.CharField(max_length=150,blank=True)
    