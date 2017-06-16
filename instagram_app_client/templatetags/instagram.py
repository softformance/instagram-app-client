import re
import requests
from django import template
from django.conf import settings
from instagram_app_client import app_settings
from urllib import unquote

# Get an instance of a logger
register = template.Library()
URL_GRAB = app_settings.BASE_URL + '/instagram_app/get_posts/'

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
    local_url = URL_GRAB + str(app_id)
    data = requests.get(local_url, params=params)
    url = getattr(settings, 'INSTAGRAM_APP_URL', 'http://stream.dillysocks.com/')
    return {'photos': data.json, 'CLASS_WIDGET': class_widget, 'url': url}
