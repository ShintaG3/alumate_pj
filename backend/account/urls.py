from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name="account"

urlpatterns = [
    # list
    path('countries', views.CountryList.as_view()),
    path('schools', views.SchoolList.as_view()),
    path('majors', views.MajorList.as_view()),
    path('goals', views.GoalList.as_view()),
    path('study-interests', views.StudyInterestList.as_view()),
    path('followings/user', views.FollowingListUser.as_view()),
    path('follweds/user', views.FollowedListUser.as_view()),
    
    # list + create
    path('basic-info', views.BasicInfoUser.as_view()),
    path('educations/user', views.EducationListUser.as_view()),
    path('goals/user', views.GoalListUser.as_view()),
    path('study-interests/user', views.StudyInterestListUser.as_view()),
    path('scholarshps/user', views.ScholarshipListUser.as_view()),
    path('social-links/user', views.SocialLinkListUser.as_view()),
    path('works/user', views.WorkExperienceListUser.as_view()),

    # retrieve / update / delete
    path('about/user', views.AboutUser.as_view()),
    path('basic-info/user', views.BasicInfoList.as_view()),
    path('profile/user', views.ProfileUser.as_view()),
    path('profile-image/user', views.ProfileImageUser.as_view()),
    
    path('educations/user', views.EducationDetailUser.as_view()),
    path('goals/user', views.GoalDetailUser.as_view()),
    path('scholarshps/user', views.ScholarshipDetailUser.as_view()),
    path('social-links/user', views.SocialLinkDetailUser.as_view()),
    path('works/user', views.WorkDetailUser.as_view()),

    # create
    path('follow/<id:int>', views.Follow.as_view())
    
    # delete
    path('unfollow/<id:int>', views.Unfollow.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)