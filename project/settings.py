import os
from environs import Env
from django.core.management.utils import get_random_secret_key

env = Env()
env.read_env()
sensitive_bd_data = {
    'bd_engine': env('DB_ENGINE'),
    'bd_host': env('DB_HOST'),
    'bd_port': env('DB_PORT'),
    'bd_name': env('DB_NAME'),
    'bd_user': env('DB_USER'),
    'bd_password': env('DB_PASSWORD'),
    'secret_key': 'SECRET_KEY'
}

DATABASES = {
    'default': {
        'ENGINE': sensitive_bd_data['bd_engine'],
        'HOST': sensitive_bd_data['bd_host'],
        'PORT': sensitive_bd_data['bd_port'],
        'NAME': sensitive_bd_data['bd_name'],
        'USER': sensitive_bd_data['bd_user'],
        'PASSWORD': sensitive_bd_data['bd_password'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = sensitive_bd_data['secret_key']

DEBUG = env.bool("DEBUG", default=False)

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
