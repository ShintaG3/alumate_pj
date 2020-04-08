from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from .views import SignupView, LoginView, BaseInquiryView

app_name="auths"

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('base-inquiry/', BaseInquiryView.as_view(), name='baseInquiry'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('base-connect/', views.baseConnect, name='baseConnect'),
    path('register/ajax/checkpwdstrength/', views.checkpwdstrength, name='checkpwdstrength')
    ]
