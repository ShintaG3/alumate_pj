from django.urls import path
from .views import PostView, PostCommentView, PostLikeView

app_name="feed"

urlpatterns = [
    path('', PostView.as_view(), name='feed'),
    path('comment/<int:post_id>', PostCommentView.as_view(), name='comment'),
    path('like/<int:post_id>', PostLikeView.as_view(), name='like'),
    
]
