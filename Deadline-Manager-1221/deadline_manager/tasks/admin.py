from django.contrib import admin

from .models import *

admin.site.register(Tag)
admin.site.register(TaskFolder)
admin.site.register(Task)
