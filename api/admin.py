from django.contrib import admin
from .models import News, CustomUser, Project

admin.site.register(News)
admin.site.register(CustomUser)
admin.site.register(Project)
