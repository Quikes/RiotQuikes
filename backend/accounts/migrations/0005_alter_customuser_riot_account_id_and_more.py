# Generated by Django 4.0.3 on 2022-04-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_riot_summoner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='riot_account_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='riot_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='riot_profileIconId',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='riot_puuid',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='riot_summoner_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]