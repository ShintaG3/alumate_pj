from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

app_name="auths"

urlpatterns = [
    path('register/', TemplateView.as_view(template_name="auths/register.html"), name='register'),
    path('register2/', views.signup, name='signup'),
    path('base-inquiry2/', views.baseInquiry, name='baseInquiry'),
    path('login/', TemplateView.as_view(template_name="auths/login.html"), name='login'),
    path('base-inquiry/', TemplateView.as_view(template_name="auths/base-inquiry.html"), name='base-inquiry'),
    path('base-connect2/', views.baseConnect, name='baseConnect'),
    path('base-connect/', TemplateView.as_view(template_name="auths/base-connect.html"), name='base-connect'),
    path('base-connect2/ajax/follow/', views.follow, name='follow')
]
