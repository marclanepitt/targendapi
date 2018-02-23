# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class University(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Course(models.Model):
	university = models.ForeignKey(University)
	department = models.CharField(max_length=6)
	semester = models.CharField(max_length=5)
	number = models.IntegerField()
	section = models.IntegerField()
	instructor = models.CharField(max_length=30)
	description = models.CharField(max_length=50)

	def __str__(self):
		return '{} {}-{} {} ({})'.format(self.department,self.number,self.section,self.description,self.semester)


#class Event(models.Model):
