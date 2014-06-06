"""
Django settings for miprimerproyecto project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.urlresolvers import reverse_lazy

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd^d+63_ggbym9$)cl3ec*=+vzoe00asp$&ke=_64r=2-e2r@n+'

# SECURITY WARNING: don't run with debug turned on in production!
# A false es para ponerlo en produccion
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'preguntasyrespuestas',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'miprimerproyecto.urls'

WSGI_APPLICATION = 'miprimerproyecto.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "miprimerproyecto/TEMPLATES"),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

##        'NAME': BASE_DIR + '/Documents and Settings/Usuario/Escritorio/PYTHON/django/Jesus Conde/video 001/miprimerproyecto/miprimerproyecto/BD/basedatos.sqlite',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '\\miprimerproyecto\\BD\\basedatos.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

LOGIN_URL = reverse_lazy('login')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
