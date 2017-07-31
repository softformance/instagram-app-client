import os
import re
from urllib import unquote

import requests
import requests_cache
from django import template
from urlparse import urljoin

from instagram_app_client import app_settings as settings

# Enabling cache
requests_cache.install_cache(
    'instagram_app_cache',
    backend=settings.STREAM_CACHING_BACKEND,
    expire_after=settings.STREAM_CACHE_EXPIRATION
)

# Get an instance of a logger
register = template.Library()


@register.inclusion_tag('instagram_app_client/instagram_photos.html', takes_context=True)
def show_posts(context, tags, app_id=settings.INSTAGRAM_APP_ID, count=None, order_by=None, class_widget=None):
    """
    {% show_posts app_id=1 tags='test,dilly' %}
    """
    params = {}
    tags = unquote(tags)
    tags = re.findall(r"[\w']+", tags.lower())
    params['tags'] = tags
    params['count'] = str(count)
    params['order_by'] = order_by
    local_url = urljoin(settings.STREAM_URL, os.path.join('/instagram_app/get_posts/', str(app_id)))

    try:
        if settings.STREAM_ENABLED:
            data = requests.get(local_url, params=params)
            data = data.json()  # Will fail silently here in case of any issues
            return {
                'photos': data,
                'CLASS_WIDGET': class_widget,
                'url': settings.STREAM_URL
            }
        else:
            return {}
    except:
        return {}
