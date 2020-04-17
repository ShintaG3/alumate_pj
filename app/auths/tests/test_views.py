from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'myuser'
        self.url = reverse('auths:register')
        self.data = {
            'password1': 'valid_password1',
            'password2': 'valid_password1',
            'email': 'email@test.com',
            'username': self.username
        }
        self.bad_data = self.data.copy()
        self.bad_data.update({'password2': 'badpassword'})
        self.register_button = '<button type="submit" class="btn btn-primary mt-4" id="registerUser" disabled=true>Create account</button>'

    def test_register_registers_valid_user(self):
        self.client.post(self.url, self.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, self.username)

    def test_register_redirects_after_registration(self):
        response = self.client.post(self.url, self.data, follow = True)
        self.assertRedirects(response, reverse('accounts:base-inquiry'))

    def test_register_returns_form_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed('register.html')
        self.assertInHTML(
            self.register_button,
            str(response.content)
        )

    def test_register_returns_form_for_invalid(self):
        response = self.client.post(self.url, self.bad_data)
        self.assertTemplateUsed('register.html')
        self.assertInHTML(
            self.register_button,
            str(response.content)
        )
    
    def test_register_returns_form_error_for_invalid(self):
        response = self.client.post(self.url, self.bad_data)
        self.error_message = "Error Alert:"
        self.assertInHTML(
            self.error_message,
            str(response.content)
        )

    def test_view__register_url_exists_at_desired_location(self):
        response = self.client.get('/auths/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_register_url_accessible_by_name(self):
        response = self.client.get(reverse('auths:register'))
        self.assertEqual(response.status_code, 200)

    def test_view_register_uses_correct_template(self):
        response = self.client.get(reverse('auths:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auths/register.html')


class LoginViewTestCase(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='hellyeah20', password='hello@2020')
        test_user1.save()
        self.client = Client()
        self.url = reverse('auths:login')

    def test_login_functionality(self):
        self.data = {
            'username':'hellyeah20', 
            'password':'hello@2020'
        }
        response = self.client.post(self.url, self.data)
        self.assertRedirects(response, reverse('feed:feed'))

    def test_view_login_url_exists_at_desired_location(self):
        response = self.client.get('/auths/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_login_url_accessible_by_name(self):
        response = self.client.get(reverse('auths:login'))
        self.assertEqual(response.status_code, 200)

    def test_view_login_uses_correct_template(self):
        response = self.client.get(reverse('auths:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auths/login.html')