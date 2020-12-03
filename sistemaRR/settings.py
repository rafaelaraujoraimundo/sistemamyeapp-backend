"""
Django settings for sistemaRR project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0s3^)s3xotyvj19nv^)h2dvcs4r+k@*!!&9gd*8z7(d-%n06)%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # PLUGIN
    'bootstrapform',
    'django_celery_results',
    'django_celery_beat',
    'drf_yasg',
    'corsheaders',
    
    # JWT LOGIN TOKEN
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    
    # PACOTES REST FRAMEWORK
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    
    # MODULO
    'core',
    'av.api',
    'av.avcadastro',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sistemaRR.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'sistemaRR.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dbdjvqlnccdapj",
        "USER": "ehdxvcohtbpvwh",
        "PASSWORD": "8b11f93eb1666afb5bc349531507f36eb93e3a0dae95c293d6ab87301cec1ea8",
        "HOST": "ec2-54-163-47-62.compute-1.amazonaws.com",
        "PORT": 5432,
    }
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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Alterar modelo de usuarios padrões

AUTH_USER_MODEL = 'core.CustomUsuario'

# Arquivos Estaticos

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Redirect do Login_requiride

LOGIN_REDIRECT_URL = ''

LOGOUT_REDIRECT_URL = ''

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': 'global',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1000,
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '99/minute',
        'user': '99/minute'
    }
}

# JWT settings
REST_USE_JWT = True

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=60),
}

SITE_ID=1

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'av.api.serializers.UsuarioSerializer',
}
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://floating-brook-29227.herokuapp.com",
    "http://127.0.0.1:9000"
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
)


# Habilitar Heroku
import django_heroku
django_heroku.settings(locals())
