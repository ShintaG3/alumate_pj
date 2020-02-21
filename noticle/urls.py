from django.urls import path
from django.views.generic import TemplateView

app_name="noticle"

urlpatterns = [
    path('', TemplateView.as_view(template_name="noticle/noticle.html"), name='noticle'),
]