"""targendaapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""familyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.users.v1.views import RegistrationView, KnoxLoginView,PasswordResetFixView

v1_urls = [
    url(r'^users/', include('apps.users.v1.urls', namespace='users')),
    url(r'^courses/', include('apps.courseselect.v1.urls',namespace="courses")),
    url(r'^calendar/', include('apps.tarcalendar.v1.urls',namespace="calendar")),
]

api_urls = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/login/',KnoxLoginView.as_view(),name="knox_login_hi"),
    url(r'^auth/password/reset/$', PasswordResetFixView.as_view(), name="password_reset"),
    url(r'^auth/', include('knox.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/$', RegistrationView.as_view(), name="rest_register"),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^allauth/', include('allauth.urls')),
    url(r'^drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/', include(v1_urls, namespace='v1')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)