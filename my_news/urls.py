from django.urls import path
from . import views

app_name = 'my_news'
urlpatterns = [
    path('', views.index, name='index'),
]