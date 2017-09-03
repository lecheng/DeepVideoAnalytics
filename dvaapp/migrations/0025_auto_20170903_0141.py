# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 01:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0024_systemstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvapql',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemstate',
            name='hosts',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='systemstate',
            name='queues',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
