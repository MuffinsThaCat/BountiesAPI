# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std_bounties', '0024_auto_20190509_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftbounty',
            name='sourceDirectoryHash',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='sourceFileName',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]