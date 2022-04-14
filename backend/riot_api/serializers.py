from .models import SummonerSimpleDataFlex,SummonerSimpleDataSolo
from rest_framework import serializers

class SummonerSimpleDataSoloSerializer(serializers.ModelSerializer):

    class Meta:
        model = SummonerSimpleDataSolo
        fields = '__all__'
        # read_only_fields = ('name',)
        
class SummonerSimpleDataFlexSerializer(serializers.ModelSerializer):

    class Meta:
        model = SummonerSimpleDataFlex
        fields = '__all__'
        # read_only_fields = ('name',)