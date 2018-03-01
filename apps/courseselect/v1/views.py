from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated

from . import serializers
from ..models import Course

class CourseListView(generics.ListAPIView):
	serializer_class = serializers.CourseSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		queryset = Course.objects.filter(university=self.kwargs['university'])
		department = self.request.query_params.get('department', None)
		if department is not None:
			queryset = queryset.filter(department=department)
		number = self.request.query_params.get('number', None)
		if number is not None:
			queryset = queryset.filter(number=number)
		section = self.request.query_params.get('section', None)
		if section is not None:
			queryset = queryset.filter(section=section)
		return queryset