# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='population',
            name='population',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
