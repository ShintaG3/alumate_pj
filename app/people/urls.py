from django.urls import path, re_path
from .views import PeopleView

app_name="people"

urlpatterns = [
    re_path(r'^', PeopleView.as_view(), name="index"),
]
