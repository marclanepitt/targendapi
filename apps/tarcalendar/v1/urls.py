from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^request/', views.UserCalendarRequestView.as_view(), name='cal-request'),
]
