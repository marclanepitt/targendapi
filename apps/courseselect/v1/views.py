from rest_framework import generics,mixins
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response



from . import serializers
from ..models import Course

class CourseListView(generics.ListAPIView):
	serializer_class = serializers.CourseSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		queryset = Course.objects.filter(university=self.kwargs['university']).order_by('department', 'number')
		department = self.request.query_params.get('department', None)
		if department is not None:
			queryset = queryset.filter(department=department)
		number = self.request.query_params.get('number', None)
		if number is not None:
			queryset = queryset.filter(number=number)
		section = self.request.query_params.get('section', None)
		if section is not None:
			queryset = queryset.filter(section=section)
		semester = self.request.query_params.get('semester', None)
		if semester is not None:
			queryset = queryset.filter(semester=semester)
		return queryset

class CourseFilterOptionsView(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def get(self,request):
		departments = Course.objects.order_by().values('department').distinct()
		semesters = Course.objects.order_by().values('semester').distinct()
		numbers = Course.objects.order_by().values('number').distinct()
		sections = Course.objects.order_by().values('section').distinct()
		total_dict = {}

		dep_list = []
		for d in departments:
			dep_list.append({'value':d['department'],'label':d['department']})
		total_dict['department']=dep_list

		sem_list = []
		for d in semesters:
			new = ""
			year = "20"
			if(d['semester'][0] is 'S'):
				new = "Spring"
			else:
				new = "Fall"
			year = year + d['semester'][1] + d['semester'][2]
			sem_list.append({'value':d['semester'],'label':new+ " " + year})
		total_dict['semester']=sem_list

		num_list = []
		for d in numbers:
			num_list.append({'value':d['number'],'label':d['number']})
		total_dict['number']=num_list

		sect_list = []
		for d in sections:
			sect_list.append({'value':d['section'],'label':d['section']})

		total_dict['section']=sect_list

		return Response(total_dict)