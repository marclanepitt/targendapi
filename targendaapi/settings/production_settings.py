import os
from .settings import BASE_DIR

DEBUG = False
CORS_ORIGIN_ALLOW_ALL = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST','*')]

EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')