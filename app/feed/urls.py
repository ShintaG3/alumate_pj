from django.urls import path
from .views import *

app_name="feed"

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('post/comment/<int:post_id>', PostCommentView.as_view(), name='comment'),
    path('post/like/<int:post_id>', PostLikeView.as_view(), name='like-post'),
    path('comment/like/<int:comment_id>', PostCommentLikeView.as_view(), name='like-comment'),
    path('post', PostView.as_view(), name='comment'),
    path('ask', AskView.as_view(), name='ask'),
]
