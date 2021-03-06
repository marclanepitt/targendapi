# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-23 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseselect', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='year_in_school',
            new_name='university',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]
