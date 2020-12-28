from django.contrib import admin
from .models import Article, Post

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    list_filter = ["title", "created"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["article", "creator", "created"]
    search_fields = ["creator"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Post, PostAdmin)
