from django.urls import path
from django.views.generic import TemplateView

from .views import Index 
namespace="demo" 

urlpatterns = [
    path('', Index, name="demo"),
    path('index', TemplateView.as_view(template_name="demo/index.html")),
    path('examples/landing', TemplateView.as_view(template_name="demo/examples/landing.html")),
    path('examples/login', TemplateView.as_view(template_name="demo/examples/login.html")),
    path('examples/profile', TemplateView.as_view(template_name="demo/examples/profile.html")),
    path('examples/register', TemplateView.as_view(template_name="demo/examples/register.html")),
]