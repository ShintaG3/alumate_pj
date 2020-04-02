from django.urls import path
from django.views.generic import TemplateView

app_name="message"

urlpatterns = [
    path('', TemplateView.as_view(template_name="message/message-list.html"), name='message_list'),
]