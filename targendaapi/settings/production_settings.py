import os
from .settings import BASE_DIR

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['class-cal-api.herokuapp']

EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')