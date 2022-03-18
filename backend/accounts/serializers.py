from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id','username','email','riot_name','riot_account_id','riot_puuid','riot_profileIconId','riot_summonerLevel','riot_summoner_id')
        read_only_fields = ('riot_account_id','riot_puuid','riot_profileIconId','riot_summonerLevel','riot_summoner_id')
        
class CustomUserUpdaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk','riot_name','riot_account_id','riot_puuid','riot_profileIconId','riot_summonerLevel','riot_summoner_id')
        read_only_fields = ('riot_account_id','riot_puuid','riot_profileIconId','riot_summonerLevel','riot_summoner_id')