from django.urls import path
from django.views.generic import TemplateView
from .views import MessageListView, MessageDetailView

app_name="message"

urlpatterns = [
    path('', MessageListView.as_view(), name='index'),
    path('send-new-message', MessageListView.as_view(), name='send-new-message'),
    path('detail/<str:username_to>', MessageDetailView.as_view(), name='message_detail'),
    path('send-reply/<str:username_to>', MessageDetailView.as_view(), name='send-reply'),
]