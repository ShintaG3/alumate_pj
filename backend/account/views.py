from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


# list view

class CountryList(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer

    def get_queryset(self):
        params = self.request.GET
        queryset = super().get_queryset()
        starts_with = params.get('starts-with', None)
        if starts_with:
            queryset = queryset.filter(name__istartswith=starts_with)
        return queryset


class SchoolList(generics.ListAPIView):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer

    def get_queryset(self):
        params = self.request.GET
        queryset = super().get_queryset()
        starts_with = params.get('starts-with', None)
        if starts_with:
            queryset = queryset.filter(name__istartswith=starts_with)
        return queryset


class MajorList(generics.ListAPIView):
    queryset = models.Major.objects.all()
    serializer_class = serializers.MajorSerializer

    def get_queryset(self):
        params = self.request.GET
        queryset = super().get_queryset()
        starts_with = params.get('starts-with', None)
        if starts_with:
            queryset = queryset.filter(name__istartswith=starts_with)
        return queryset


class GoalList(generics.ListAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer


class StudyInterestList(generics.ListAPIView):
    queryset = models.StudyInterest.objects.all()
    serializer_class = serializers.StudyInterestSerializer


class FollowingListUser(generics.ListAPIView):
    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer

    def get_queryset(self):
        user = self.request.user
        return user.following_users


class FollowedListUser(generics.ListAPIView):
    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer

    def get_queryset(self):
        user = self.request.user
        return user.followed_users


# list create view

class BasicInfoList(generics.ListCreateAPIView):
    queryset = models.BasicInfo.objects.all()
    serializer_class = serializers.BasicInfoSerializer


class EducationListUser(generics.ListCreateAPIView):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer

    def get_queryset(self):
        user = self.request.user
        return user.educations


class GoalListUser(generics.ListCreateAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer

    def get_queryset(self):
        user = self.request.user
        return user.goals.all()


class StudyInterestListUser(generics.ListCreateAPIView):
    queryset = models.StudyInterest.objects.all()
    serializer_class = serializers.StudyInterestSerializer

    def get_queryset(self):
        user = self.request.user
        return user.study_interests.all()


class ScholarshipListUser(generics.ListCreateAPIView):
    queryset = models.Scholarship.objects.all()
    serializer_class = serializers.ScholarshipSerializer

    def get_queryset(self):
        user = self.request.user
        return user.scholarships


class SocialLinkListUser(generics.ListCreateAPIView):
    queryset = models.SocialLink.objects.all()
    serializer_class = serializers.SocialLinkSerializer

    def get_queryset(self):
        user = self.request.user
        return user.social_links


class WorkExperienceListUser(generics.ListCreateAPIView):
    queryset = models.WorkExperience.objects.all()
    serializer_class = serializers.WorkExperienceSerializer

    def get_queryset(self):
        user = self.request.user
        return user.works


# detail view (one to one)

class AboutUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        return get_object_or_404(queryset, user=user)


class BasicInfoUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BasicInfo.objects.all()
    serializer_class = serializers.BasicInfoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        return get_object_or_404(queryset, user=user)


class ProfileUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        return get_object_or_404(queryset, user=user)


class ProfileImageUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProfileImage.objects.all()
    serializer_class = serializers.ProfileImageSerializer

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        return get_object_or_404(queryset, user=user)


# detail view (one to many)


class EducationDetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj_id = self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class GoalDetailUser(generics.RetrieveDestroyAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj_id = self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)

class StudyInterestDetailUser(generics.RetrieveDestroyAPIView):
    queryset = models.StudyInterest.objects.all()
    serializer_class = serializers.StudyInterestSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj_id = self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class ScholarshipDetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Scholarship.objects.all()
    serializer_class = serializers.ScholarshipSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj_id = self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class SocialLinkDetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SocialLink.objects.all()
    serializer_class = serializers.SocialLinkSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj_id = self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


class WorkDetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WorkExperience.objects.all()
    serializer_class = serializers.WorkExperienceSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj_id = self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, id=obj_id)


# create

class Follow(APIView):
    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowCreateSerializer

    def post(self, request, pk=None):
        user = request.user
        follow_user = get_object_or_404(User, pk=pk)
        try:
            follow = models.Follow.objects.get(follower=user, followed=follow_user)
            serializer = self.serializer_class(post_like)
            return Response(serializer.data, status=status.HTTP_303_SEE_OTHER)
        except models.Follow.DoesNotExist: # normal case
            follow = models.Follow.objects.create(follower=user, followed=follow_user)
            serializer = self.serializer_class(follow)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# destroy


class Unfollow(generics.DestroyAPIView):
    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer

    def get_object(self):
        queryset = self.get_queryset()
        following_id =self.kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, follower=user, followed=following_id)
