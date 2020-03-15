from django.urls import path
from django.views.generic import TemplateView
from .views import ContactView

app_name="index"

urlpatterns = [
    path('', TemplateView.as_view(template_name="landingpage/index.html"), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
]