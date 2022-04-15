from django.forms import ValidationError
import requests
import os
from config.settings import CACHE_TTL, RIOT_API_KEY
from .serializers import (
    SummonerSimpleDataFlexSerializer,
    SummonerSimpleDataSoloSerializer,
)
from .models import SummonerSimpleDataSolo, SummonerSimpleDataFlex
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from helpers.account_update_from_username import user_update

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth import get_user_model


class SummonerSimpleDataSoloViewset(viewsets.ModelViewSet):
    Authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]
    serializer = SummonerSimpleDataSoloSerializer

    def get_queryset(self):
        user = self.request.user
        if user is None:
            pass
        return SummonerSimpleDataSolo.objects.filter(user=user)

    # @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    # def update_user_from_riotusername(self, request,pk=None):
    #     user = get_user_model().objects.get(pk=pk)
    #     if user:
    #         user.riot_name = request.POST.get('riot_name')
    #         user.save()
    #         user = user_update(user)

    #         serializer = self.get_serializer_class()
    #         return Response(serializer(user, many=False).data)
    #     else:
    #         raise ValidationError

    def get_serializer_class(self):
        # if self.action=='update_user_from_riotusername':
        #     return SummonerSimpleDataSolo
        return SummonerSimpleDataSoloSerializer


class SummonerSimpleDataFlexViewset(viewsets.ModelViewSet):
    Authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]
    serializer = SummonerSimpleDataSoloSerializer

    def get_queryset(self):
        user = self.request.user
        return SummonerSimpleDataFlex.objects.filter(user=user)

    def get_serializer_class(self):
        return SummonerSimpleDataFlexSerializer
