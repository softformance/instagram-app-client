import requests
from django import template
from instagram_app_client import app_settings
from urllib import unquote
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
register = template.Library()
URL_GRAB = app_settings.BASE_URL + '/instagram_app/get_posts/'

@register.inclusion_tag('instagram_app_client/instagram_photos.html', takes_context=True)
def show_posts(context, tags, app_id=app_settings.INSTAGRAM_APP_ID, count=None, order_by=None, class_widget=None):
    """
    {% show_posts app_id=1 tags='test,dilly' %}
    """
    params = {}
    tags = unquote(tags)
    tags = [element.lower() for element in tags.split(', ')]
    params['tags'] = tags
    params['count'] = str(count)
    logger.error("Ordering by %s" % order_by)
    params['order_by'] = str('Test: %s' % order_by)
    local_url = URL_GRAB + str(app_id)
    data = requests.get(local_url, params=params)
    return {'photos': data.json, 'CLASS_WIDGET': class_widget}
