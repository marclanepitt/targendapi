# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Course, CourseImage, University

admin.site.register(Course)
admin.site.register(University)
admin.site.register(CourseImage)