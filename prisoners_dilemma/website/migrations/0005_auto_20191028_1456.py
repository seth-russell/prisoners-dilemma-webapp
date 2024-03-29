# Generated by Django 2.2.2 on 2019-10-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20191028_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_player_one_unregistered',
            field=models.BooleanField(default=False, verbose_name='Is player one not logged in'),
        ),
        migrations.AddField(
            model_name='game',
            name='is_player_two_unregistered',
            field=models.BooleanField(default=False, verbose_name='Is player two not logged in'),
        ),
    ]
