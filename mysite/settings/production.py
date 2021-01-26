from .base import *
import os
import django_heroku, dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
}
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

django_heroku.settings(locals())