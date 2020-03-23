from django.urls import path
from django.views.generic import TemplateView

from .views import Index 
app_name = 'demo'

urlpatterns = [
    path('', Index, name="demo"),
    path('index', TemplateView.as_view(template_name="demo/index.html"), name='index'),
    path('examples/landing', TemplateView.as_view(template_name="demo/examples/landing.html"), name='landing'),
    path('examples/login', TemplateView.as_view(template_name="demo/examples/login.html"), name='login'),
    path('examples/profile', TemplateView.as_view(template_name="demo/examples/profile.html"), name='profile'),
    path('examples/register', TemplateView.as_view(template_name="demo/examples/register.html"), name='register'),
]