from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name="account"

urlpatterns = [
    # list
    path('countries', views.CountryList.as_view(), name='countries'),
    path('schools', views.SchoolList.as_view(), name='schools'),
    path('majors', views.MajorList.as_view(), name='majors'),
    path('goals', views.GoalList.as_view(), name='goals'),
    path('study-interests', views.StudyInterestList.as_view(), name='study-interests'),
    path('followings/user', views.FollowingListUser.as_view(), name='user-following'),
    path('follweds/user', views.FollowedListUser.as_view(), name='user-followed'),
    
    # list + create
    path('basic-info', views.BasicInfoList.as_view(), name='basic-info'),
    path('educations/user', views.EducationListUser.as_view(), name='user-educations'),
    path('goals/user', views.GoalListUser.as_view(), name='user-goals'),
    path('study-interests/user', views.StudyInterestListUser.as_view(), name='user-study-interests'),
    path('scholarshps/user', views.ScholarshipListUser.as_view(), name='user-scholarships'),
    path('social-links/user', views.SocialLinkListUser.as_view(), name='user-social-links'),
    path('works/user', views.WorkExperienceListUser.as_view(), name='user-works'),

    # retrieve / update / delete
    path('about/user', views.AboutUser.as_view(), name='user-about'),
    path('basic-info/user', views.BasicInfoUser.as_view(), name='user-basic-info'),
    path('profile/user', views.ProfileUser.as_view(), name='user-profile'),
    path('profile-image/user', views.ProfileImageUser.as_view(), name='user-profile-image'),
    
    path('educations/user/<int:id>', views.EducationDetailUser.as_view(), name='user-education'),
    path('scholarshps/user/<int:id>', views.ScholarshipDetailUser.as_view()),
    path('social-links/user/<int:id>', views.SocialLinkDetailUser.as_view()),
    path('works/user/<int:id>', views.WorkDetailUser.as_view()),

    # retrieve / destroy
    path('goals/user/<int:id>', views.GoalDetailUser.as_view(), name='user-goal'),
    path('study-interests/user/<int:id>', views.StudyInterestDetailUser.as_view(), name='user-study-interest'),

    # create
    path('follow/<int:id>', views.Follow.as_view()),
    
    # delete
    path('unfollow/<int:id>', views.Unfollow.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)