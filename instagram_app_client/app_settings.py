from django.conf import settings
from constance import config

BASE_URL = getattr(settings, 'BASE_URL', 'http://stream.dillysocks.com')
INSTAGRAM_APP_ID = getattr(settings, 'INSTAGRAM_APP_ID', 1)
STREAM_URL = getattr(
    config, 'INSTAGRAM_STREAM_URL', 'http://stream.dillysocks.com/')
STREAM_ENABLED = getattr(config, 'INSTAGRAM_STREAM_ENABLED', True)
STREAM_ENABLE_CACHING = getattr(config, 'INSTAGRAM_STREAM_ENABLE_CACHING', True)
STREAM_CACHE_EXPIRATION = getattr(
    config, 'INSTAGRAM_STREAM_CACHE_EXPIRATION', 60 * 10)  # 10 min by default
STREAM_CACHING_BACKEND = getattr(
    settings, 'INSTAGRAM_STREAM_CACHING_BACKEND', 'memory')
IG_CLIENT_LOGGING = getattr(settings, 'IG_CLIENT_LOGGING', True)
ROOT_DIR = settings.PROJECT_DIR
