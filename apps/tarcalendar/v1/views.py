from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

import pygsheets

from . import serializers

class UserCalendarRequestView(APIView):
	authentication_classes = (IsAuthenticated,)

	def get(self,request):
		gc = pygsheets.authorize()
		sh = gc.open("Targenda Calendar Requests")
		wks = sh.worksheet_by_title("Sheet1")
		for row in wks:
  			cd print(row)