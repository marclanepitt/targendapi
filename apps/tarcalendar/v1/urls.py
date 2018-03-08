from django.conf.urls import url

from . import views

app_name="calendar"

urlpatterns = [
    url(r'^request', views.UserCalendarRequestView.as_view(), name='cal-request'),
    url(r'^cancel', views.UserCalendarUndoView.as_view(), name='cal-undo'),
]
