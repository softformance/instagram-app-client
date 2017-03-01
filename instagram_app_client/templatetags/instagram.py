import requests
from django import template

register = template.Library()
BASE_URL = 'http://insta-dev.softformance.com/'
URL_GRAB = BASE_URL + 'instagram_app/get_posts/'
USER_AUTH_DATA = 'instagram-app'
PASS_AUTH_DATA = 'app-instagram'

@register.inclusion_tag('instagram_app_client/instagram_photos.html', takes_context=True)
def show_posts(context, app_id, tags, count=5, order_by='created_at'):
    """
    {% show_posts app_id=1 tags='test,dilly' %}
    """
    request = context['request']
    grab_url = URL_GRAB + str(app_id) + '?tags=' + str(tags) \
            + "&count=" + str(count) + "&order_by=" + str(order_by)
    print(grab_url)
    if USER_AUTH_DATA and PASS_AUTH_DATA:
        data = requests.get(grab_url, auth=(USER_AUTH_DATA, PASS_AUTH_DATA))
    else:
        data = requests.get(grab_url)
    return {'photos': data.json}