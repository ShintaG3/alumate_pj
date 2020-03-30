from django.urls import path
from .views import PostView, PostCommentView

app_name="feed"

urlpatterns = [
    path('', PostView.as_view(), name='feed'),
    path('comment/<int:post_id>', PostCommentView.as_view(), name='comment'),
]
