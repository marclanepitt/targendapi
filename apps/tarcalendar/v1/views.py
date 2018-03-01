from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import pygsheets

from . import serializers

class UserCalendarRequestView(APIView):
	authentication_classes = (IsAuthenticated,)

	def get(self,request):
		try:
			gc = pygsheets.authorize()
			sh = gc.open("Targenda Calendar Requests")
			wks = sh.worksheet_by_title("Sheet1")
			values = []
			pk = self.request.query_params.get('id', None)
			profile = get_object_or_404(UserProfile,user= pk)
			user = get_object_or_404(User,pk=pk)
			values.append(user.email)
			for course in profile.courses.all():
				values.append('{} {}-{} {} ({})'.format(course.department,course.number,course.section,course.description,course.semester))
			values.append("new")
			wks.insert_rows(row=0, number=1, values=values)
			return Response({"success":True})
		except Exception as err:
			raise err