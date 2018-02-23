from rest_framework import serializers,exceptions
from django.shortcuts import get_object_or_404

from apps.courseselect.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("__all__")