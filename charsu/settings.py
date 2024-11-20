"""
Django settings for charsu project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
from datetime import timedelta
from pathlib import Path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '74957888-43bf-47a7-8231-024c4791aaca'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#user service use diffrent auth
AUTH_USER_MODEL = 'user_service.UserInfo'
# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My APPs
    'rest_framework',
    'rest_framework_simplejwt',
    'django_extensions',
    'user_service',
    'product_service',
    'order_service',
    'payment_service',
    'notification_service',
    'debug_toolbar',
    'corsheaders',
]
#Add restframworrk to setting
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        ),
        
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
        ),    
    }
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
    }
# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

ROOT_URLCONF = 'charsu.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'charsu.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'charsu_group',
        'USER': 'postgres',
        'PASSWORD': '123yhbpoi123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
#logging Dictionary Configuration\
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            
            },
            'file':{
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug.log',
                },    
        },
    'loggers':{
        'django':{
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
            '':{
                'handlers': ['console','file'],
                'level': 'DEBUG',
                },    
        },    
    }
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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

#FrontEnd project URL
CORS_ALLOWED_ORIGIN = [
        'http://localhost:3000'
    ]
INTERNAL_IPS = [
    '127.0.0.1',
    ]



# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
