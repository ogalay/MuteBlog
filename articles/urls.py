from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('reply/<int:article_id>', views.post_reply, name='reply'),
    path('article/<int:article_id>', views.show_article, name='article'),
    path('new', views.new_article, name='new_article')
]