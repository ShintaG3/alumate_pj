from django.urls import path
from django.views.generic import TemplateView

app_name="auths"

urlpatterns = [
    path('register/', TemplateView.as_view(template_name="auths/register.html"), name='register'),
    path('login/', TemplateView.as_view(template_name="auths/login.html"), name='login'),
    path('base-inquiry/', TemplateView.as_view(template_name="auths/base-inquiry.html"), name='base-inquiry'),
    path('base-connect/', TemplateView.as_view(template_name="auths/base-connect.html"), name='base-connect'),
]