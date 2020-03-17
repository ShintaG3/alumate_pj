from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

app_name="auths"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('setting/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('base-inquiry/', views.baseInquiry, name='baseInquiry'),
    path('login/', TemplateView.as_view(template_name="auths/login.html"), name='login'),
    path('base-connect/', views.baseConnect, name='baseConnect'),
    path('base-connect/ajax/follow/', views.follow, name='follow')
    ]
