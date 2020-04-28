from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from .views import SignupView, LoginView

app_name="auths"

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('base-connect/', views.baseConnect, name='baseConnect'),
    path('register/ajax/checkpwdstrength/', views.checkpwdstrength, name='checkpwdstrength'),
    path('privacy-policy/', TemplateView.as_view(template_name='auths/privacypolicy.html'), name='privacy-policy')
    ]
