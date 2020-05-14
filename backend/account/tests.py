from django.test import TestCase
from rest_framework import status
from . import models, views
from django.urls import reverse
from django.contrib.auth.models import User
from alumate_api.test import get_auth_client


class CountryTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:countries')

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


class BasicInfoTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:basic-info')
        self.user = User.objects.get(username='testuser')
        country1 = models.Country.objects.create(name='Japan')
        country2 = models.Country.objects.create(name='Canada')
        user1 = User.objects.create(username='user1', password='testing1')
        self.user_basic_info = models.BasicInfo.objects.create(
            user=user1, name='testname', status=models.CurrentStatus.CURRENT_STUDENT, country_origin=country1, country_study_abroad=country2)

        self.data = {
            'name': 'client',
            'status': models.CurrentStatus.CURRENT_STUDENT,
            'country_origin': country1.id,
            'country_study_abroad': country2.id
        }

    def test_api_get_all_basic_info(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_create_user_basic_info(self):
        self.assertEqual(models.BasicInfo.objects.count(), 1)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.BasicInfo.objects.count(), 2)


class EducationTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-educations')
        self.user = User.objects.get(username='testuser')

        major = models.Major.objects.create(name='computer science')
        school1 = models.School.objects.create(name='University of smth1')
        school2 = models.School.objects.create(name='University of smth2')

        education = models.Education.objects.create(
            user=self.user, degree=models.DegreeStatus.BACHELOR, school=school1, major=major, is_study_abroad=False)

        self.data = {
            'degree': models.DegreeStatus.BACHELOR,
            'school': school2.id,
            'major': major.id,
            'is_study_abroad': False
        }

    def test_api_get_user_educations_cannot_get_other_users(self):
        self.assertEqual(models.Education.objects.count(), 1)
        models.Education.objects.create(
            user=User.objects.create(
                username='another_user', password='foranotheruser'),
            school=models.School.objects.create(
                name='something else university'),
            major=models.Major.objects.create(name='some major'),
            degree=models.DegreeStatus.BACHELOR,
            is_study_abroad=False
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_get_user_educations(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_create_user_educations(self):
        self.assertEqual(models.Education.objects.count(), 1)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Education.objects.count(), 2)


class GoalTestCase(TestCase):
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-goals')
        self.user = User.objects.get(username='testuser')

        goal = models.Goal.objects.create(user=self.user, body='some goal')

        self.data = {
            'body': 'another goal'
        }

    def test_api_get_user_goals_cannot_get_other_users(self):
        self.assertEqual(models.Goal.objects.count(), 1)
        models.Goal.objects.create(
            user=User.objects.create(
                username='another_user', password='foranotheruser'),
            body='another user goal'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_get_user_goals(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_create_user_goal(self):
        self.assertEqual(models.Goal.objects.count(), 1)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Goal.objects.count(), 2)


class StudyInterestTestCase(TestCase):
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-study-interests')
        self.user = User.objects.get(username='testuser')

        study_interest = models.StudyInterest.objects.create(
            user=self.user, body='some study interest')

        self.data = {
            'body': 'another study interest'
        }

    def test_api_get_user_study_interests_cannot_get_other_users(self):
        self.assertEqual(models.StudyInterest.objects.count(), 1)
        models.StudyInterest.objects.create(
            user=User.objects.create(
                username='another_user', password='foranotheruser'),
            body='another user study interest'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_get_user_study_interests(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_create_user_study_interest(self):
        self.assertEqual(models.StudyInterest.objects.count(), 1)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.StudyInterest.objects.count(), 2)


class ScholarshipTestCase(TestCase):
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-scholarships')
        self.user = User.objects.get(username='testuser')

        scholarship = models.Scholarship.objects.create(
            user=self.user, organization='Some organization', title='Some Title')

        self.data = {
            'organization': 'Another organization',
            'title': 'Another Title'
        }

    def test_api_get_user_scholarships_cannot_get_other_users(self):
        self.assertEqual(models.Scholarship.objects.count(), 1)
        models.Scholarship.objects.create(
            user=User.objects.create(
                username='another_user', password='foranotheruser'),
            organization='Some organization',
            title='Some Title'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_get_user_scholarships(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_create_user_scholarship(self):
        self.assertEqual(models.Scholarship.objects.count(), 1)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Scholarship.objects.count(), 2)


class SocialLinkTestCase(TestCase):
    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:user-social-links')
        self.user = User.objects.get(username='testuser')

        social_link = models.SocialLink.objects.create(
            user=self.user, title='Some Title', url='http://something.com')

        self.data = {
            'title': 'Another Title',
            'url': 'http://another.com'
        }

    def test_api_get_user_social_links_cannot_get_other_users(self):
        self.assertEqual(models.SocialLink.objects.count(), 1)
        models.SocialLink.objects.create(
            user=User.objects.create(
                username='another_user', password='foranotheruser'),
            title='Some Title',
            url='http://something.com'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_get_user_social_links(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_api_create_user_social_link(self):
        self.assertEqual(models.SocialLink.objects.count(), 1)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.SocialLink.objects.count(), 2)
