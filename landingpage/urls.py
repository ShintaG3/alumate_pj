from django.urls import path
from django.views.generic import TemplateView

app_name="index"

urlpatterns = [
    path('', TemplateView.as_view(template_name="landingpage/index.html"), name='index'),
    path('contact/', TemplateView.as_view(template_name="landingpage/contact.html"), name='contact'),
]