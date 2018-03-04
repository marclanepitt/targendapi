from rest_framework import serializers,exceptions
from ..models import CalendarRequest

class CalendarRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = CalendarRequest
		fields =('__all__')