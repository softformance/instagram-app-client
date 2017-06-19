import re
import requests
from django import template
from django.conf import settings
from instagram_app_client import app_settings
from urllib import unquote
from urlparse import urljoin
from ..models import *


# Get an instance of a logger
register = template.Library()

STREAM_SETTINGS = GlobalInstagramFeedSetings.objects.get()

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
    local_url = urljoin(STREAM_SETTINGS.stream_url, '/instagram_app/get_posts/', str(app_id))

    try:
        if STREAM_SETTINGS.stream_enabled:
            data = requests.get(local_url, params=params)
            return {
                'photos': data.json,
                'CLASS_WIDGET': class_widget,
                'url': STREAM_SETTINGS.stream_url
            }
        else:
            return {}
    except:
        return {}
