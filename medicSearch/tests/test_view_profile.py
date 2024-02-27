from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from medicSearch.models import Profile
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.edit_profile_url = reverse('edit_profile')

        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        # self.profile = Profile.objects.create(
        #     user=self.user,
        #     first_name='John',
        #     last_name='Doe',
        #     email='john.doe@example.com'
        # )

    def test_edit_profile_view_get_request(self):
        self.client.login(username='testuser', password='password')

        response = self.client.get(self.edit_profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['profileForm'], UserProfileForm)
        self.assertIsInstance(response.context['userForm'], UserForm)
        self.assertIsNone(response.context['message'])

    def test_edit_profile_view_post_request_valid_data(self):
        self.client.login(username='testuser', password='password')

        response = self.client.post(self.edit_profile_url, {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['profileForm'], UserProfileForm)
        self.assertIsInstance(response.context['userForm'], UserForm)
        self.assertEqual(response.context['message'], {'type': 'success', 'text': 'Dados atualizados com sucesso'})
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, 'Jane')
        self.assertEqual(self.profile.last_name, 'Smith')
        self.assertEqual(self.profile.email, 'jane.smith@example.com')

    def test_edit_profile_view_post_request_invalid_data(self):
        self.client.login(username='testuser', password='password')

        response = self.client.post(self.edit_profile_url, {
            'first_name': '',
            'last_name': '',
            'email': ''
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['profileForm'], UserProfileForm)
        self.assertIsInstance(response.context['userForm'], UserForm)
        self.assertEqual(response.context['message'], {'type': 'danger', 'text': 'Dados inválidos'})
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, 'John')
        self.assertEqual(self.profile.last_name, 'Doe')
        self.assertEqual(self.profile.email, 'john.doe@example.com')

    def test_edit_profile_view_post_request_duplicate_email(self):
        self.client.login(username='testuser', password='password')

        response = self.client.post(self.edit_profile_url, {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'john.doe@example.com'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertIsInstance(response.context['profileForm'], UserProfileForm)
        self.assertIsInstance(response.context['userForm'], UserForm)
        self.assertEqual(response.context['message'], {'type': 'warning', 'text': 'E-mail já usado por outro usuário'})
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, 'John')
        self.assertEqual(self.profile.last_name, 'Doe')
        self.assertEqual(self.profile.email, 'john.doe@example.com')