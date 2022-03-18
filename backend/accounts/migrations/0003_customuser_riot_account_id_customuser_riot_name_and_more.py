# Generated by Django 4.0.3 on 2022-03-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_super_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='riot_account_id',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='riot_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='riot_profileIconId',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='riot_puuid',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='riot_summonerLevel',
            field=models.PositiveIntegerField(null=True),
        ),
    ]