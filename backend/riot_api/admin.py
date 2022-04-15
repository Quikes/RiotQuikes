from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from riot_api.models import SummonerSimpleDataSolo, SummonerSimpleDataFlex

# Register your models here.
@admin.register(SummonerSimpleDataSolo)
class SummonerSimpleDataSoloAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    pass


@admin.register(SummonerSimpleDataFlex)
class SummonerSimpleDataFlexAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    pass
