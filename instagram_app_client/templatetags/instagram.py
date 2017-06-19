import re
import requests
from django import template
from django.conf import settings
from instagram_app_client import app_settings
from urllib import unquote
from urlparse import urljoin
from constance import config


# Get an instance of a logger
register = template.Library()

STREAM_URL = getattr(config, 'INSTAGRAM_STREAM_URL', 'http://stream.dillysocks.com/')
STREAM_ENABLED = getattr(config, 'INSTAGRAM_STREAM_ENABLED', True)


@register.inclusion_tag('instagram_app_client/instagram_photos.html', takes_context=True)
def show_posts(context, tags, app_id=app_settings.INSTAGRAM_APP_ID, count=None, order_by=None, class_widget=None):
    """
    {% show_posts app_id=1 tags='test,dilly' %}
    """
    params = {}
    tags = unquote(tags)
    tags = re.findall(r"[\w']+", tags.lower())
    params['tags'] = tags
    params['count'] = str(count)
    params['order_by'] = order_by
    local_url = urljoin(STREAM_URL, '/instagram_app/get_posts/', str(app_id))

    try:
        if STREAM_ENABLED:
            data = requests.get(local_url, params=params)
            data = data.json # Will fail silently here in case of any issues
            return {
                'photos': data,
                'CLASS_WIDGET': class_widget,
                'url': STREAM_URL
            }
        else:
            return {}
    except:
        return {}
