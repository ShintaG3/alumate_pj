from django.urls import path
from django.views.generic import TemplateView

app_name="inquiry"

urlpatterns = [
    path('', TemplateView.as_view(template_name="inquiry/inquiry.html"), name="inquiry"),
    path('detail', TemplateView.as_view(template_name="inquiry/inquiry-detail.html"), name="inquiry-detail"),
]
