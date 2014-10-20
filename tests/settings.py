import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'push.sqlite'),
    },
}

INSTALLED_APPS = (
    'django.contrib.sites',
    'tests.publisher',
    'tests.subscriber',
)

STATIC_URL = '/static/'

SECRET_KEY = 'test secret key'

ROOT_URLCONF = ''

SITE_ID = 1

PUSH_DOMAIN = 'testserver.com'