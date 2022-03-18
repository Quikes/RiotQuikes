import requests

from config.settings import CACHE_TTL,RIOT_API_KEY
from django.contrib.auth import get_user_model


def user_update(user):
    if user.riot_name :

        api_key = RIOT_API_KEY
        params = {'api_key':api_key}
        r= requests.get(f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user.riot_name}',params,timeout=2)

        print(r.json())
        if r.status_code == 200:
            text = r.json()

            user.riot_account_id=text['accountId']
            user.riot_puuid = text['puuid']
            user.riot_summonerLevel = text['summonerLevel']
            user.riot_summoner_id = text['id']
            
            user.save()
            
            return user
        else:
            return 'wrong username'
    else:
        return 'error'