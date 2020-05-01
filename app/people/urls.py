from django.urls import path
from .views import PeopleView, update_result, FollowView

app_name="people"

urlpatterns = [
    path('search', update_result, name="search"),
    path('follow/<int:id>', FollowView.as_view(), name='follow'),
    path('', PeopleView.as_view(), name="index"),
]
