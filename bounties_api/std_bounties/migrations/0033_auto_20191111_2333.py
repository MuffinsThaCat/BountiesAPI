# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-11 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std_bounties', '0032_auto_20191111_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
