from django.urls import path, include
from django.views.generic import TemplateView

app_name="account"

urlpatterns = [
    path('', TemplateView.as_view(template_name="account/account.html"), name="account"),
    path('edit/', TemplateView.as_view(template_name="account/account-edit.html"), name="account-edit"),
]
