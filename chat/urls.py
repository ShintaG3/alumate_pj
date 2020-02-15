from django.urls import path
from django.views.generic import TemplateView

app_name="chat"

urlpatterns = [
    path('', TemplateView.as_view(template_name="chat/chat.html"), name="chat"),
]
