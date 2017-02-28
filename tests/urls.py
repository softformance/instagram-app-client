# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from instagram_app_client.urls import urlpatterns as instagram_app_client_urls

urlpatterns = [
    url(r'^', include(instagram_app_client_urls, namespace='instagram_app_client')),
]
