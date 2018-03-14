import os
from .settings import INSTALLED_APPS

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
INSTALLED_APPS = INSTALLED_APPS + [
    'raven.contrib.django.raven_compat',
]