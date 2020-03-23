from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

app_name="auths"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('base-inquiry/', views.baseInquiry, name='baseInquiry'),
    url('login/', auth_views.LoginView, {'template_name': 'auths/login.html'}, name='login'),
    path('base-connect/', views.baseConnect, name='baseConnect'),
    path('base-connect/ajax/follow/', views.follow, name='follow')
    ]
