# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	UNCCH = 'UNC-CH'
	UNIVERSITIES = (
		(UNCCH, 'UNC Chapel Hill'),
	)
	year_in_school = models.CharField(
		max_length=5,
		choices=UNIVERSITIES,
		default=UNCCH,
	)
	semester = models.CharField(max_length=5)
	number = models.IntegerField()
	section = models.IntegerField()

#class Event(models.Model):
