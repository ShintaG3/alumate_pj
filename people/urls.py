from django.urls import path
from django.views.generic import TemplateView

app_name="people"

urlpatterns = [
    path('', TemplateView.as_view(template_name="people/people.html"), name="people"),
]
