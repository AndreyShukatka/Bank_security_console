import os
from environs import Env

env = Env()
env.read_env()
bd_engine = env('ENGINE')
bd_host = env('HOST')
bd_port = env('PORT')
bd_name = env('NAME')
bd_user = env('USER')
bd_password = env('PASSWORD')


DATABASES = {
    'default': {
        'ENGINE': bd_engine,
        'HOST': bd_host,
        'PORT': bd_port,
        'NAME': bd_name,
        'USER': bd_user,
        'PASSWORD': bd_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
