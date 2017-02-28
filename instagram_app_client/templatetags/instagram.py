import requests
from django import template

register = template.Library()

BASE_URL = 'http://insta-dev.softformance.com/instagram_app/get_posts/'

@register.inclusion_tag('instagram-app-client/instagram_photos.html', takes_context=True)
def show_posts(context, app_id, tags, count=5, order_by='created_at'):
    """
    {% show_posts app_id=1 tags='test,dilly' %}
    """
    request = context['request']
    grab_url = BASE_URL + str(app_id) + '?tags=' + str(tags) \
            + "&count=" + str(count) + "&order_by=" + str(order_by)
    print(grab_url)
    data = requests.get(grab_url)
    return {'photos': data}