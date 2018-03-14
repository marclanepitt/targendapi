"""
Django settings for targendaapi project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEV_KEY = 'h=&ob$p#6yym^%4^-nwwao^46zbt303q3kw#dm+)zt3&npbabf'
# TODO export as env var in prod
SECRET_KEY = os.environ.get('SECRET_KEY', DEV_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG',False)


# ALLOWED_HOSTS = [host.strip() for host in os.environ.get('ALLOWED_HOSTS', '').split(',')]
CORS_ALLOW_HEADERS = (
    'accept',
    'auth',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #Project Apps
    'apps.users',
    'apps.courseselect',
    'apps.tarcalendar',
    
    # 3rd party apps
    'django_extensions',
    'rest_framework',
    'django_filters',
    'crispy_forms',
    'knox',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'targendaapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'targendaapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

API_VERSIONS = ['v1']
DEFAULT_VERSION = 'v1'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'dist')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_VERSION': DEFAULT_VERSION,
    'ALLOWED_VERSIONS': API_VERSIONS,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

REST_KNOX = {
    'USER_SERIALIZER': 'apps.users.v1.serializers.UserDetailRestKnoxFix',
}

LOGOUT_ON_PASSWORD_CHANGE = False
OLD_PASSWORD_FIELD_ENABLED = True
REST_SESSION_LOGIN  = False
REST_AUTH_TOKEN_MODEL = 'knox.models.AuthToken'
REST_AUTH_TOKEN_CREATOR = 'apps.users.v1.token_generator.generate'
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'apps.users.v1.serializers.RegistrationSerializer'
}

# Django all auth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_DISPLAY = lambda user: user.email
ACCOUNT_USERNAME_REQUIRED = False

#email config
SERVER_EMAIL = 'no.reply@classcal.com'
# Email address regular users receive mail from
DEFAULT_FROM_EMAIL = 'no.reply@classcal.com'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DJANGO_LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(DJANGO_LOGS_DIR):
    os.mkdir(DJANGO_LOGS_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(pathname)s:%(lineno)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console_simple': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_verbose': {
            'level': 'INFO',
            'filters': [],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file_verbose': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': os.path.join(DJANGO_LOGS_DIR, 'server_log.log'),
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': True,
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            'filters': ['require_debug_true'],
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console_simple'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_verbose', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'targendaapi': {
            'handlers': ['file_verbose', 'console_verbose'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

if(os.environ.get('PRODUCTION')):
    # Activate Django-Heroku.
    import django_heroku
    django_heroku.settings(locals())
    from .production_settings import *
else:
    from .local_settings import *
