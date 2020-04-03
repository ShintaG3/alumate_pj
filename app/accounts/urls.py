from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name="accounts"

urlpatterns = [
    # path('', TemplateView.as_view(template_name="account/account.html")),
    path('edit/', TemplateView.as_view(template_name="account/account-edit.html"), name="account-edit"),
    path('base-inquiry/', BaseInquiryView.as_view(), name="base-inquiry"),
    path('<str:username>/update/basic-info', BasicInfoUpdateView.as_view(), name="update-basic-info"),
    path('<str:username>/update/goals', GoalUpdateView.as_view(), name="update-goals"),
    path('<str:username>/update/study-interests', StudyInterestUpdateView.as_view(), name="update-study-interests"),
    path('<str:username>/update/about', AboutUpdateView.as_view(), name="update-about"),
    path('<str:username>/update/education', EducationUpdateView.as_view(), name="update-education"),
    path('<str:username>/update/education/<int:pk>', EducationUpdateView.as_view(), name="update-education"),
    path('<str:username>/update/work', WorkExperienceUpdateView.as_view(), name="update-work"),
    path('<str:username>/update/work/<int:pk>', WorkExperienceUpdateView.as_view(), name="update-work"),
    
    path('<str:username>/', AccountView.as_view(), name="account-page"),
]

