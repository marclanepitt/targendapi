# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-24 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseselect', '0005_course_department'),
        ('users', '0003_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='courses',
            field=models.ManyToManyField(to='courseselect.Course'),
        ),
    ]
