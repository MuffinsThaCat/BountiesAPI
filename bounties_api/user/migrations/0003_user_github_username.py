# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180614_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github_username',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
