from django.conf.urls import url

from . import views

app_name="courses"

urlpatterns = [
    url(r'^list/(?P<university>\d)', views.CourseListView.as_view(), name='course-list'),
    url(r'^filters', views.CourseFilterOptionsView.as_view(), name='course-filters'),
]
