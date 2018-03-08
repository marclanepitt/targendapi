from django.db import models
from django import forms
from django.contrib.auth.models import User
from ..courseselect.models import Course
from ..tarcalendar.models import CalendarRequest

class UserProfile(models.Model):
    major = models.CharField(max_length =30)
    graduation_year = models.DateField(auto_now_add=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    cal_request = models.OneToOneField(CalendarRequest, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

