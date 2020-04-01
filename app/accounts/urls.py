from django.urls import path, include
from django.views.generic import TemplateView
from .views import AccountView, BasicInfoUpdateView, GoalUpdateView, StudyInterestUpdateView

app_name="accounts"

urlpatterns = [
    # path('', TemplateView.as_view(template_name="account/account.html")),
    path('edit/', TemplateView.as_view(template_name="account/account-edit.html"), name="account-edit"),
    path('<str:username>/update/profile', BasicInfoUpdateView.as_view(), name="update-basic-info"),
    path('<str:username>/update/goals', GoalUpdateView.as_view(), name="update-goals"),
    path('<str:username>/update/study-interests', StudyInterestUpdateView.as_view(), name="update-study-interests"),
    path('<str:username>/', AccountView.as_view(), name="account-page"),
]

