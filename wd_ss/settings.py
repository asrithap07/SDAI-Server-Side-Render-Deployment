"""
Django settings for wd_ss project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os

import dj_database_url

import dotenv

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['sdai-server-side-render-deployment.onrender.com', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://sdai-server-side-render-deployment.onrender.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'detection',
    'rest_framework.authtoken',

    'alertupload_rest',
    'rest_framework',
    'django_filters',
    'django_extensions',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wd_ss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wd_ss.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
 
'''
DATABASES = {
        'default': {
            #'ENGINE': 'django.db.backends.sqlite3',
            'ENGINE': 'django.db.backends.postgresql',
            #'NAME': BASE_DIR / 'db.sqlite3',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': '5432',
        }
    }
'''

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#added underscore between static and root
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

load_dotenv()

#SMTP Configuration

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'gmail_utils.GmailOAuth2Backend'
#EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email host
#EMAIL_PORT = 587  # This is for TLS. Use 465 for SSL.
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
#DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']

#OAuth2 settings
#GMAIL_CLIENT_ID = os.environ['GMAIL_CLIENT_ID']
#GMAIL_CLIENT_SECRET = os.environ['GMAIL_CLIENT_SECRET']
#GMAIL_REFRESH_TOKEN = os.environ['GMAIL_REFRESH_TOKEN']

#Twilio configuration

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']

#Sinch configuration
SINCH_PROJECT_ID = os.environ['SINCH_PROJECT_ID']
SINCH_KEY_SECRET = os.environ['SINCH_KEY_SECRET']
SINCH_KEY_ID = os.environ['SINCH_KEY_ID']
SINCH_NUMBER = os.environ['SINCH_NUMBER']

#Textmagic configuration
TEXTMAGIC_USERNAME = os.environ['TEXTMAGIC_USERNAME']
TEXTMAGIC_API_KEY = os.environ['TEXTMAGIC_API_KEY']

#Amazon s3 configuration
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'safedetectai'
AWS_S3_REGION_NAME = 'us-east-2'
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}


AWS_LOCATION = 'static'
AWS_S3_CUSTOM_DOMAIN = 'safedetectai.s3.us-east-2.amazonaws.com'
PUBLIC_MEDIA_LOCATION = 'media/images/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}'
DEFAULT_FILE_STORAGE = 'wd_ss.storage_backends.PublicMediaStorage'

AWS_DEFAULT_ACL = None  # Try setting this to 'private' if None doesn't work
AWS_BUCKET_ACL = None  # Same here, try 'private' if None doesn't work