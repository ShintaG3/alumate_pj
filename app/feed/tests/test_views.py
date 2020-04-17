# Feed
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class FeedViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user1 = User.objects.create_user(username='hellyeah20', password='hello@2020')
        
        self.test_user1.save()

    def test_redirect_if_not_logged_in_for_feed(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertRedirects(response, '/auths/login/?next=/feed/')
    
    def test_logged_in_uses_correct_template_for_feed(self):
        login = self.client.login(username='hellyeah20', password='hello@2020')
        response = self.client.get(reverse('feed:feed'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'hellyeah20')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/feed.html')

    def test_post_function_for_post(self):
        self.client.force_login(self.test_user1)
        self.url = reverse('feed:feed')
        self.user = self.test_user1
        self.data = {
            'user': self.user,
            'body': 'Hello world!!'
        }
        self.message = self.data['body']
        response = self.client.post(self.url, self.data, follow=True)
        self.assertEqual(response.status_code, 200)