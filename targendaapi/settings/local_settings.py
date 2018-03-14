import os
from .settings import BASE_DIR

DEBUG = True

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# https://docs.djangoproject.com/en/1.10/ref/databases/#caveats

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,
}

# If INTERNAL_IPS becomes a problem, can override SHOW_TOOLBAR_CALLBACK function
# See https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html#debug-toolbar-config
INTERNAL_IPS = ['127.0.0.1', 'localhost']
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'c2d573d0bb5e43'
EMAIL_HOST_PASSWORD = '8ba6f95986c533'
EMAIL_PORT = '2525'