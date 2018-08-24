# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_user_github_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_hash',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_touched_manually',
            field=models.BooleanField(default=False),
        ),
    ]
