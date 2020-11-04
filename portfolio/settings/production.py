from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

WAGTAIL_SITE_NAME = 'Jakobs Portfolio'

DEBUG = True

with open('/home/projects/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()