from django.db import models
from django import forms
from django.contrib.auth.models import User

class UserProfile(models.Model):
    major = models.CharField(max_length =30)
    graduation_year = models.DateField(auto_now_add=False)
    user = models.OneToOneField(User)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

