from django.urls import path
from .views import *

app_name="feed"

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('post/comment/<int:id>', PostCommentView.as_view(), name='comment-post'),
    path('post/like/<int:id>', PostLikeView.as_view(), name='like-post'),
    path('post/comment/like/<int:id>', PostCommentLikeView.as_view(), name='like-post-comment'),
    path('post', PostView.as_view(), name='create-post'),
    path('ask/like/<int:id>', AskLikeView.as_view(), name='like-ask'),
    path('ask', AskView.as_view(), name='create-ask'),
]
