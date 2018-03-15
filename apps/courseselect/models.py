# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class University(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class CourseImage(models.Model):
	image = models.CharField(max_length=500)

	def __str__(self):
		return self.image.name

class Course(models.Model):
	university = models.ForeignKey(University,on_delete=models.CASCADE)
	department = models.CharField(max_length=6)
	semester = models.CharField(max_length=5)
	number = models.IntegerField()
	section = models.IntegerField()
	instructor = models.CharField(max_length=30)
	description = models.CharField(max_length=50)
	assignment_total = models.IntegerField()
	lecture_total = models.IntegerField()
	test_total = models.IntegerField()

	image = models.ForeignKey(CourseImage,on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}-{} {} ({})'.format(self.department,self.number,self.section,self.description,self.semester)

#class Event(models.Model):