from django.urls import path
from .views import HomeView, ContactView

app_name="index"

urlpatterns = [
    path('', HomeView.as_view(template_name="landingpage/index.html"), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
]