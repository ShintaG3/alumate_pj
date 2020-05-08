from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name="account"

urlpatterns = [
    # list / create
    path('', views.PostList.as_view()),
    path('comments/<int:id>/', views.PostCommentList.as_view()),
    path('likes/<int:id>/', views.PostLikeList.as_view()),
    path('comment/likes/<int:id>/', views.PostCommentLikeList.as_view()),

    # retrieve / update / delete
    path('<int:id>/', views.PostList.as_view()),
    path('comments/<int:id>/', views.PostCommentList.as_view()),
    path('like/<int:id>/', views.PostLikeList.as_view()),
    path('comment/like/<int:id>/', views.PostCommentLikeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)