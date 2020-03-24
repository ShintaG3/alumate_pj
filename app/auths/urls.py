from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

app_name="auths"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('base-inquiry/', views.baseInquiry, name='baseInquiry'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('base-connect/', views.baseConnect, name='baseConnect'),
    path('base-connect/ajax/follow/', views.follow, name='follow')
    ]
