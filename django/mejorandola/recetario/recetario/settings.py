#encoding: utf-8

"""
Django settings for recetario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# The ID, as an integer, of the current site in the django_site database table. 
# This is used so that application data can hook into specific sites and a single database 
# can manage content for multiple sites.
SITE_ID = 1 # O cualquier otra ID numerica de tu sitio

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wc%joegugxs%_7(jk**m6r(hu%*i&j)nnm=!s(9e%*ki_qh617'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

"""
Cuando Django tiene la opcion de DEBUG=False, las notificaciones de error de
codigo deben ser enviadas via correo electronico a los administradores, junto con
los detalles completos del error. Para poner los datos de los administradores
debemos buscar la siguiente porcion:
ADMINS = (
  ('Your Name', 'your_email@example.com'),
)
"""
ADMINS = (
    ('Jeronimo Sanchez', 'socger@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'recetario.urls'

WSGI_APPLICATION = 'recetario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'BD\BD.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'recetario',
#         'USER': 'root',
#         'PASSWORD': 'RegSoc',
#         'HOST': '127.0.0.1',
#         'PORT': '3307',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# CONFIGURACION DEL IDIOMA
# Django tambien permite configurar el idioma que usara de manera predeterminada
# para su funcionamiento
LANGUAGE_CODE = 'es-ES'

# ZONA HORARIA
# Django permite configurar la zona horaria del proyecto# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# En esta sección le estamos diciendo que debe buscar las plantillas dentro de la
# carpeta del proyecto, en una carpeta llamada plantillas, como esta carpeta aún no
# existe debemos crearla manualmente dentro de recetario.
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "PLANTILLAS"),
)


# La clase Receta (modelo) tiene un atributo imagen, el cuál está direccionando las
# cargas que haga el usuario a la carpeta ‘recetas’ (carpeta que estará dentro de
# otra llamada: ‘carga’)
MEDIA_ROOT = os.path.join(BASE_DIR,'CARGA')


