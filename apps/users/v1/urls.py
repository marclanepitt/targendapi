from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+|me)', views.UserDetailView.as_view(), name='profile-detail'),
    url(r'^profile', views.UserProfileCreateView.as_view(), name='profile-create'),
    url(r'^list', views.UserProfileListView.as_view(), name='profile-detail'),
    url(r'^course-add', views.UserCourseAddView.as_view(), name='course-add'),
    url(r'^course-remove', views.UserCourseRemoveView.as_view(), name='course-remove'),

]
