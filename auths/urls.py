from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views


app_name="auths"

urlpatterns = [
    path('register/', TemplateView.as_view(template_name="auths/register.html"), name='register'),
    path('signup/', views.signup, name='signup'),
    path('userprofile/', views.userProfile, name='userprofile'),
    path('login/', TemplateView.as_view(template_name="auths/login.html"), name='login'),
    path('base-inquiry/', TemplateView.as_view(template_name="auths/base-inquiry.html"), name='base-inquiry'),
    path('base-connect/', views.baseConnect, name='base-connect'),
]



