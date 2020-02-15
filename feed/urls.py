from django.urls import path
from django.views.generic import TemplateView

app_name="feed"

urlpatterns = [
    path('', TemplateView.as_view(template_name="feed/feed.html"), name='feed'),

]
