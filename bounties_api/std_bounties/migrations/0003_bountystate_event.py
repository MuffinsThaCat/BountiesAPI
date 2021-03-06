# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-18 22:15
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('std_bounties', '0002_auto_20180409_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='BountyState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bountyStage', models.IntegerField()),
                ('change_date', models.DateTimeField()),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='std_bounties.Bounty')),
            ],
            options={
                'get_latest_by': 'change_date',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=128)),
                ('fulfillment_id', models.IntegerField(null=True)),
                ('transaction_hash', models.CharField(max_length=128)),
                ('transaction_from', models.CharField(max_length=128)),
                ('contract_inputs', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('event_date', models.DateTimeField()),
                ('bounty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='std_bounties.Bounty')),
            ],
        ),
    ]
