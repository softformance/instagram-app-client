import requests
from django import template
from django.conf import settings

register = template.Library()
URL_GRAB = settings.BASE_URL + '/instagram_app/get_posts/'
USER_AUTH_DATA = 'instagram-app'
PASS_AUTH_DATA = 'app-instagram'

@register.inclusion_tag('instagram_app_client/instagram_photos.html', takes_context=True)
def show_posts(context, app_id, tags, count=None, order_by=None):
    """
    {% show_posts app_id=1 tags='test,dilly' %}
    """
    params = {}
    tags = [element.lower() for element in tags.split(', ')]
    params['tags'] = tags
    params['count'] = str(count)
    params['order_by'] = str(order_by)
    local_url = URL_GRAB + str(app_id)
    if USER_AUTH_DATA and PASS_AUTH_DATA:
        data = requests.get(local_url, auth=(USER_AUTH_DATA, PASS_AUTH_DATA), params=params)
    else:
        data = requests.get(local_url, params=params)
    return {'photos': data.json}