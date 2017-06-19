from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import *

admin.site.register(GlobalInstagramFeedSetings, SingletonModelAdmin)
