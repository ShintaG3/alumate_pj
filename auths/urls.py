from django.urls import path
from django.views.generic import TemplateView

app_name="auths"

urlpatterns = [
    path('register/', TemplateView.as_view(template_name="auths/register.html"), name='register'),
    path('login/', TemplateView.as_view(template_name="auths/login.html"), name='login'),
]