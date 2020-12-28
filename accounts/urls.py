from django.urls import path

from .views import signup, logout_view, login_page

app_name = 'accounts'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
]