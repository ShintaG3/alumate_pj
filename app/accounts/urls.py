from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name="accounts"

urlpatterns = [
    # path('', TemplateView.as_view(template_name="account/account.html")),
    # path('edit/', TemplateView.as_view(template_name="account/account-setting.html"), name="account-setting"),
    path('base-inquiry/', BaseInquiryView.as_view(), name="base-inquiry"),
    path('follow/<str:username>', FollowView.as_view(), name="follow"),
    path('unfollow/<str:username>', UnfollowView.as_view(), name="unfollow"),
    path('<str:username>/update/basic-info', BasicInfoUpdateView.as_view(), name="update-basic-info"),
    path('<str:username>/update/profile-image', UploadProfileImageView.as_view(), name="upload-profile-image"),
    path('<str:username>/update/goals', GoalUpdateView.as_view(), name="update-goals"),
    path('<str:username>/update/study-interests', StudyInterestUpdateView.as_view(), name="update-study-interests"),
    path('<str:username>/update/about', AboutUpdateView.as_view(), name="update-about"),
    path('<str:username>/add/education', EducationCreateView.as_view(), name="add-education"),
    path('<str:username>/update/education/<int:pk>', EducationUpdateView.as_view(), name="update-education"),
    path('<str:username>/add/work', WorkExperienceUpdateView.as_view(), name="add-work"),
    path('<str:username>/update/work/<int:pk>', WorkExperienceUpdateView.as_view(), name="update-work"),
    path('<str:username>/add/scholarship/', ScholarShipView.as_view(), name="add-scholarship"),
    path('<str:username>/update/scholarship/<int:pk>', ScholarShipView.as_view(), name="update-scholarship"),
    path('<str:username>/add/social-link', SocialLinkView.as_view(), name="add-social-link"),
    path('<str:username>/update/social-link/<int:pk>', SocialLinkView.as_view(), name="update-social-link"),
    path('<str:username>/update/profile', ProfileView.as_view(), name="update-profile"),
    path('<str:username>/add/study-abroad', CreateStudyAbroad.as_view(), name="add-study-abroad"),
    path('<str:username>/update/study-abroad', SelectStudyAbroad.as_view(), name="update-study-abroad"),
    path('<str:username>/post/comment/<int:id>', PostCommentView.as_view(), name='comment-post'),
    path('<str:username>/post/like/<int:id>', PostLikeView.as_view(), name='like-post'),
    path('<str:username>/post/comment/like/<int:id>', PostCommentLikeView.as_view(), name='like-post-comment'),
    path('<str:username>/inquiry/like/<int:id>', InquiryLikeView.as_view(), name="inquiry-like"),
    path('<str:username>/', AccountView.as_view(), name="account-page"),
]

