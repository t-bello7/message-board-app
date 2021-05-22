"""
Production settings for django
"""

import environ 

from config.settings.base import *

env = environ.Env(
    DEBUG = (bool, False)
)

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOST')

DATABASES = {
    'default': env.db(),
}
