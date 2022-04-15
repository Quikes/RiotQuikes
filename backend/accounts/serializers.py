from .models import CustomUser
from riot_api.serializers import (
    SummonerSimpleDataSoloSerializer,
    SummonerSimpleDataFlexSerializer,
)
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    solo_data = SummonerSimpleDataSoloSerializer(source="user_data_solo", many=False)

    flex_data = SummonerSimpleDataFlexSerializer(source="user_data_flex", many=False)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "riot_name",
            "riot_account_id",
            "riot_puuid",
            "riot_profileIconId",
            "riot_summonerLevel",
            "riot_summoner_id",
            "solo_data",
            "flex_data",
        )
        read_only_fields = (
            "riot_account_id",
            "riot_puuid",
            "riot_profileIconId",
            "riot_summonerLevel",
            "riot_summoner_id",
            "solo_data",
            "flex_data",
        )


class CustomUserUpdaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "pk",
            "riot_name",
            "riot_account_id",
            "riot_puuid",
            "riot_profileIconId",
            "riot_summonerLevel",
            "riot_summoner_id",
        )
        read_only_fields = (
            "riot_account_id",
            "riot_puuid",
            "riot_profileIconId",
            "riot_summonerLevel",
            "riot_summoner_id",
        )
