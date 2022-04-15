import requests
from riot_api.models import SummonerSimpleDataFlex, SummonerSimpleDataSolo

from config.settings import CACHE_TTL, RIOT_API_KEY
from django.contrib.auth import get_user_model


def user_update(user):

    if user.riot_name:

        api_key = RIOT_API_KEY
        params = {"api_key": api_key}
        r = requests.get(
            f"https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user.riot_name}",
            params,
            timeout=2,
        )
        # print(r.url)
        # print(r.json())
        if r.status_code == 200:
            text = r.json()
            # if text["revison_date"] == user.riot_revison_date:
            #     return "User is up to date."
            user.riot_account_id = text["accountId"]
            user.riot_puuid = text["puuid"]
            user.riot_summonerLevel = text["summonerLevel"]
            user.riot_summoner_id = text["id"]
            user.riot_revision_date = text["revisionDate"]

            user.save()
            try:
                solo = SummonerSimpleDataSolo.objects.get(user=user)
            except:
                solo = SummonerSimpleDataSolo.objects.create()
                user.user_data_solo = solo
            try:
                flex = SummonerSimpleDataFlex.objects.get(user=user)
            except:
                flex = SummonerSimpleDataFlex.objects.create()
                user.user_data_flex = flex

            r2 = requests.get(
                f"https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{user.riot_summoner_id}",
                params,
                timeout=2,
            )

            data = r2.json()
            flex_data = dict(data[0])
            solo_data = dict(data[1])
            # print(solo_data.get("tier"))

            print(solo_data["tier"])
            solo.tier = solo_data["tier"]
            solo.rank = solo_data["rank"]
            solo.leaguePoints = solo_data["leaguePoints"]
            solo.wins = solo_data["wins"]
            solo.losses = solo_data["losses"]
            solo.veteran = solo_data["veteran"]
            solo.inactive = solo_data["inactive"]
            solo.fresh_blood = solo_data["freshBlood"]
            solo.hot_streak = solo_data["hotStreak"]

            solo.save()

            flex.tier = flex_data["tier"]
            flex.rank = flex_data["rank"]
            flex.leaguePoints = flex_data["leaguePoints"]
            flex.wins = flex_data["wins"]
            flex.losses = flex_data["losses"]
            flex.veteran = flex_data["veteran"]
            flex.inactive = flex_data["inactive"]
            flex.fresh_blood = flex_data["freshBlood"]
            flex.hot_streak = flex_data["hotStreak"]

            flex.save()

            return user
        else:
            return "wrong username"
    else:
        return "error"
