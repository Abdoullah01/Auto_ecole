from django.urls import path
from app_auth.views import *
from . import views


urlpatterns = [
    path('login', views.login_blog, name = 'login-blog'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout_blog, name = 'logout'),
    
]
