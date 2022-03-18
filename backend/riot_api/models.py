from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class SummonerSimpleDataSolo(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user_data_solo',null=True,on_delete=models.SET_NULL,blank=True)
    tier =  models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    summonerId= models.CharField(max_length=255)
    summonerName= models.CharField(max_length=255)
    leaguePoints =  models.IntegerField(null=True)
    wins =  models.IntegerField(null=True)
    losses =  models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)


class SummonerSimpleDataFlex(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user_data_flex',null=True,on_delete=models.SET_NULL,blank=True)
    tier =  models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    summonerId= models.CharField(max_length=255)
    summonerName= models.CharField(max_length=255)
    leaguePoints =  models.IntegerField(null=True)
    wins =  models.IntegerField(null=True)
    losses =  models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)