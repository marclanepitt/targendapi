from django.db import models

class CalendarRequest(models.Model):
	pending = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)