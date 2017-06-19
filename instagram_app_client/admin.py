from django.contrib import admin
from solo.admin import SingletonModelAdmin
from instagram_app_client.models import *

admin.site.register(GlobalInstagramFeedSetings, SingletonModelAdmin)
