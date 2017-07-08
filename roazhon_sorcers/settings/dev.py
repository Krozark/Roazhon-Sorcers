import os

from roazhon_sorcers.settings.base import *

SECRET_KEY = '6)9!5x!bmk9s_5%8*tn$2uin0i6v2y34b7!ainw$yd^wfd_6$&'

DEV = True
DEBUG = DEV
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


EMAIL_HOST = "127.0.0.1"
EMAIL_PORT = 25
EMAIL_HOST_USER = "ures"
EMAIL_HOST_PASSWORD = "pass"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
