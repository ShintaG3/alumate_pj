from django.urls import path
from django.views.generic import TemplateView
from .views import InquiryView, InquiryDetailView, InquiryLikeView, InquiryCommentLikeView, InquiryCommentView, FollowView, update_result

app_name="inquiry"

urlpatterns = [
    path('', InquiryView.as_view(), name="inquiry"),
    path('detail/<int:id>', InquiryDetailView.as_view(), name="detail"),
    path('like/<int:id>', InquiryLikeView.as_view(), name="like"),
    path('comment/like/<int:ask_id>/<int:comment_id>', InquiryCommentLikeView.as_view(), name="like-comment"),
    path('comment/<int:id>', InquiryCommentView.as_view(), name="comment"),
    path('follow/<int:id>/<str:username>', FollowView.as_view(), name="follow"),
    path('update-result', update_result, name="update-result"),
]
