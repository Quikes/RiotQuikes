# Generated by Django 4.0.3 on 2022-04-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riot_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summonersimpledataflex',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='summonersimpledataflex',
            name='summonerId',
        ),
        migrations.RemoveField(
            model_name='summonersimpledataflex',
            name='summonerName',
        ),
        migrations.RemoveField(
            model_name='summonersimpledataflex',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='summonersimpledatasolo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='summonersimpledatasolo',
            name='summonerId',
        ),
        migrations.RemoveField(
            model_name='summonersimpledatasolo',
            name='summonerName',
        ),
        migrations.RemoveField(
            model_name='summonersimpledatasolo',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='summonersimpledataflex',
            name='fresh_blood',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledataflex',
            name='hot_streak',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledataflex',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledataflex',
            name='veteran',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledatasolo',
            name='fresh_blood',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledatasolo',
            name='hot_streak',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledatasolo',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='summonersimpledatasolo',
            name='veteran',
            field=models.BooleanField(default=False),
        ),
    ]
