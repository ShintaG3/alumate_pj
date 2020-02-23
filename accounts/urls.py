from django.urls import path, include
from django.views.generic import TemplateView

app_name="accounts"

urlpatterns = [
    path('', TemplateView.as_view(template_name="account/account.html"), name="accounts"),
    path('edit/', TemplateView.as_view(template_name="account/account-edit.html"), name="account-edit"),
]

