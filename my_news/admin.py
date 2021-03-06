from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted']


admin.site.register(News, NewsAdmin)
