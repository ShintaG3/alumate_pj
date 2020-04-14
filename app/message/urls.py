from django.urls import path
from django.views.generic import TemplateView
from .views import MessageListView

app_name="message"

urlpatterns = [
    path('', MessageListView.as_view(), name='index'),
    path('detail', TemplateView.as_view(template_name="message/message-detail.html"), name='message_detail'),
    path('send-new-message/<str:username>', MessageListView.as_view(), name='send-new-message'),
]