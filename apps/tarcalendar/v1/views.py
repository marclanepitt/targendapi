from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ..models import CalendarRequest
from apps.users.v1.serializers import UserDetailSerializer
from dateutil import tz

from . import serializers

class UserCalendarRequestView(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get(self,request):
		try:
			values = []
			pk = self.request.query_params.get('id', None)

			profile = get_object_or_404(UserProfile,user= pk)
			user = get_object_or_404(User,pk=pk)
			
			values.append(user.email)

			for course in profile.courses.all():
				values.append('{} {}-{} {} ({})'.format(course.department,course.number,course.section,course.description,course.semester))
			
			request = CalendarRequest.objects.create(pending=True,description=" ".join(str(x) for x in values))
			profile.cal_request = request
			profile.save()
			serializer = UserDetailSerializer(user)
			return Response(serializer.data)
		except Exception as err:
			raise err

class UserCalendarUndoView(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get(self,request):
		try:
			pk = self.request.query_params.get('id', None)
			user = get_object_or_404(User,pk=pk)
			profile = get_object_or_404(UserProfile,user= pk)
			request = profile.cal_request
			request.delete()
			profile.cal_request = None
			profile.save()
			serializer = UserDetailSerializer(user)
			return Response(serializer.data)

		except Exception as err:
			raise err
