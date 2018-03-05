from rest_framework import serializers,exceptions
from django.shortcuts import get_object_or_404

from apps.courseselect.models import Course,CourseImage

class CourseImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = CourseImage
		fields = ["image"]

class CourseSerializer(serializers.ModelSerializer):
	image = CourseImageSerializer()
	class Meta:
		model = Course
		fields = ['id','department','semester','number','section','instructor','description','university','assignment_total','lecture_total','test_total','image']
