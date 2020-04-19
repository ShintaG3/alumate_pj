from django.urls import path
from .views import PeopleView, update_result

app_name="people"

urlpatterns = [
    path('search', update_result, name="search"),
    path('', PeopleView.as_view(), name="index"),
]
