from django.conf import settings

#Insert here your settings const.
BASE_URL = getattr(settings, 'BASE_URL', 'http://stream.dillysocks.com')
INSTAGRAM_APP_ID = getattr(settings, 'INSTAGRAM_APP_ID', 1)