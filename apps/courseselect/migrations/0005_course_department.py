# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-23 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseselect', '0004_auto_20180223_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(default='COMP', max_length=6),
            preserve_default=False,
        ),
    ]
