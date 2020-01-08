"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3GOiEE4P3hCqZVfmN5x0G5Njqq8RvqYQm4Av7iGunMzU5iyZx5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["104.198.229.174"]


# Application definition
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.scratch',
    'apps.usuario',
    'apps.login',
    'apps.sir',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'caramba',
        'USER': 'postgres',
        'PASSWORD': 'Codename47',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'usuario.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEMPLATE_DIRS=(
    os.path.join(BASE_DIR,'templates'),
)

STATIC_ROOT = '/home/django/django_project/django_project/static'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/django/django_project/django_project/media'

# STATIC_ROOT = '/var/www/horarios/demo/assets/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'carambascratch@gmail.com'
EMAIL_HOST_PASSWORD = 'Caramba**'
EMAIL_PORT = 587

