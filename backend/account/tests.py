from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate
from . import models, views
from django.urls import reverse
from django.contrib.auth.models import User


def get_auth_client():
    user_data = {"username": "testuser", "password": "fortesting"}
    client = APIClient()
    user_response = client.post('/api/auth/users/', user_data)
    jwt_response = client.post('/api/auth/jwt/create/', user_data)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                       jwt_response.data['access'])
    return client


class CountryTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:countries')
        if models.Country.objects.count() != 0:
            models.Country.objects.clear()

    def test_api_get_all_countries(self):
        self.assertEqual(models.Country.objects.count(), 0)
        models.Country.objects.create(name='Japan')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Country.objects.count(), 1)
        models.Country.objects.create(name='USA')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Country.objects.count(), 2)

    def test_api_get_filtered_countries(self):
        self.assertEqual(models.Country.objects.count(), 0)
        models.Country.objects.create(name='Japan')
        models.Country.objects.create(name='USA')
        response = self.client.get('{}?starts-with=j'.format(self.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_cannot_create_country(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class SchoolTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:schools')
        if models.School.objects.count() != 0:
            models.School.objects.clear()

    def test_api_get_all_schools(self):
        self.assertEqual(models.School.objects.count(), 0)
        models.School.objects.create(name='UBC')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.School.objects.count(), 1)
        models.School.objects.create(name='UT')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.School.objects.count(), 2)

    def test_api_get_filtered_schools(self):
        self.assertEqual(models.School.objects.count(), 0)
        models.School.objects.create(name='UBC')
        models.School.objects.create(name='UT')
        response = self.client.get('{}?starts-with=ub'.format(self.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_cannot_create_school(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class SchoolTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:schools')
        if models.School.objects.count() != 0:
            models.School.objects.clear()

    def test_api_get_all_schools(self):
        self.assertEqual(models.School.objects.count(), 0)
        models.School.objects.create(name='UBC')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.School.objects.count(), 1)
        models.School.objects.create(name='UT')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.School.objects.count(), 2)

    def test_api_get_filtered_schools(self):
        self.assertEqual(models.School.objects.count(), 0)
        models.School.objects.create(name='UBC')
        models.School.objects.create(name='UT')
        response = self.client.get('{}?starts-with=ub'.format(self.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_cannot_create_school(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class MajorTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:majors')
        if models.Major.objects.count() != 0:
            models.Major.objects.clear()

    def test_api_get_all_majors(self):
        self.assertEqual(models.Major.objects.count(), 0)
        models.Major.objects.create(name='Arts')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Major.objects.count(), 1)
        models.Major.objects.create(name='Science')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Major.objects.count(), 2)

    def test_api_get_filtered_majors(self):
        self.assertEqual(models.Major.objects.count(), 0)
        models.Major.objects.create(name='Arts')
        models.Major.objects.create(name='Science')
        response = self.client.get('{}?starts-with=ar'.format(self.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_cannot_create_majors(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class GoalTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:goals')
        self.user = User.objects.get(username='testuser')
        if models.Goal.objects.count() != 0:
            models.Goal.objects.clear()

    def test_api_get_all_goals(self):
        self.assertEqual(models.Goal.objects.count(), 0)
        models.Goal.objects.create(user=self.user, body='aa')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Goal.objects.count(), 1)
        models.Goal.objects.create(user=self.user, body='bb')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Goal.objects.count(), 2)

    def test_api_cannot_create_goal(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class StudyInterestTestCase(TestCase):
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:study-interests')
        self.user = User.objects.get(username='testuser')
        if models.StudyInterest.objects.count() != 0:
            models.StudyInterest.objects.clear()

    def test_api_get_all_study_interest(self):
        self.assertEqual(models.StudyInterest.objects.count(), 0)
        models.StudyInterest.objects.create(user=self.user, body='aa')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.StudyInterest.objects.count(), 1)
        models.StudyInterest.objects.create(user=self.user, body='bb')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.StudyInterest.objects.count(), 2)

    def test_api_cannot_create_study_interest(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class StudyInterestTestCase(TestCase):
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:study-interests')
        self.user = User.objects.get(username='testuser')
        if models.StudyInterest.objects.count() != 0:
            models.StudyInterest.objects.clear()

    def test_api_get_all_study_interest(self):
        self.assertEqual(models.StudyInterest.objects.count(), 0)
        models.StudyInterest.objects.create(user=self.user, body='aa')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.StudyInterest.objects.count(), 1)
        models.StudyInterest.objects.create(user=self.user, body='bb')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.StudyInterest.objects.count(), 2)

    def test_api_cannot_create_study_interest(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class UserFollowingTestCase(TestCase):
    
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-following')
        self.user = User.objects.get(username='testuser')
        User.objects.create(username='user1', password='testing1')
        if models.StudyInterest.objects.count() != 0:
            models.StudyInterest.objects.clear()

    def test_api_can_get_followings(self):
        user1 = User.objects.get(username='user1')

        models.Follow.objects.create(follower=self.user, followed=user1)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        for item in response.data[0].items():
            if item[0] == 'follower':
                self.assertEqual(item[1], self.user.id)
            elif item[0] == 'followed':
                self.assertEqual(item[1], user1.id)


class UserFollowedTestCase(TestCase):
    
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-followed')
        self.user = User.objects.get(username='testuser')
        User.objects.create(username='user1', password='testing1')
        if models.StudyInterest.objects.count() != 0:
            models.StudyInterest.objects.clear()

    def test_api_can_get_followings(self):
        user1 = User.objects.get(username='user1')

        models.Follow.objects.create(follower=user1, followed=self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        for item in response.data[0].items():
            if item[0] == 'follower':
                self.assertEqual(item[1], user1.id)
            elif item[0] == 'followed':
                self.assertEqual(item[1], self.user.id)