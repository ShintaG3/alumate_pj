from rest_framework import serializers
from . import models

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'


class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicInfo
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Major
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Goal
        fields = '__all__'


class StudyInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyInterest
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkExperience
        fields = '__all__'


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scholarship
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scholarship
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scholarship
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileImage
        fields = '__all__