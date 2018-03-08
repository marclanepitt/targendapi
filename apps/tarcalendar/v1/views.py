from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ..models import CalendarRequest
from apps.users.v1.serializers import UserDetailSerializer
from dateutil import tz
import pygsheets

from . import serializers

class UserCalendarRequestView(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get(self,request):
		try:
			gc = pygsheets.authorize()
			sh = gc.open("Targenda Calendar Requests")
			wks = sh.worksheet_by_title("data_dump")
			values = []
			pk = self.request.query_params.get('id', None)

			profile = get_object_or_404(UserProfile,user= pk)
			user = get_object_or_404(User,pk=pk)
			
			request = CalendarRequest.objects.create(pending=True)
			values.append(user.email)
			values.append("new")

			utc = request.date
			to_zone = tz.gettz('America/New_York')
			corrected_date = utc.astimezone(to_zone)
			values.append("{:%m/%d/%Y %H:%M:%S}".format(corrected_date))


			for course in profile.courses.all():
				values.append('{} {}-{} {} ({})'.format(course.department,course.number,course.section,course.description,course.semester))
			wks.insert_rows(row=0, number=1, values=values)
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
			gc = pygsheets.authorize()
			sh = gc.open("Targenda Calendar Requests")
			wks = sh.worksheet_by_title("data_dump")
			pk = self.request.query_params.get('id', None)
			profile = get_object_or_404(UserProfile,user= pk)
			user = get_object_or_404(User,pk=pk)
			request = get_object_or_404(CalendarRequest,pk=profile.cal_request.id)
			values = []
			values.append(user.email)
			values.append("cancelled")

			utc = request.date
			to_zone = tz.gettz('America/New_York')
			corrected_date = utc.astimezone(to_zone)
			values.append("{:%m/%d/%Y %H:%M:%S}".format(corrected_date))

			wks.insert_rows(row=0, number=1, values=values)
			request.delete()
			profile.cal_request = None
			profile.save()
			serializer = UserDetailSerializer(user)
			return Response(serializer.data)
		except Exception as err:
			raise err