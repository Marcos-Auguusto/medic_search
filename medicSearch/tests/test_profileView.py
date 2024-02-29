from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from medicSearch.models import Profile
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.edit_profile_url = reverse('edit_profile')
        self.profile = Profile.objects.get_or_create(user=User.objects.create_user(username='testuser',\
                                                     password='testpassword'))

    def test_edit_profile_valid_data(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(self.edit_profile_url, {
            'username': 'testuser1',
            'email': 'email@example.com',
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dados atualizados com sucesso')
        
    def test_edit_profile_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(self.edit_profile_url, {
            'username': '',  # Invalid data
            'email': 'newemail@example.com',
            # Include other required fields in the request
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dados inválidos')

    def test_edit_profile_duplicate_email(self):
        self.client.login(username='testuser', password='testpassword')

        # Create another user with the same email as the test user
        User.objects.create_user(username='anotheruser', password='anotherpassword', email='newemail@example.com')

        response = self.client.post(self.edit_profile_url, {
            'username': 'newusername',
            'email': 'newemail@example.com',
            # Include other required fields in the request
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'E-mail já usado por outro usuário')

    # def test_edit_profile_unauthenticated_user(self):
    #     response = self.client.post(self.edit_profile_url, {
    #         'username': 'newusername',
    #         'email': 'newemail@example.com',
    #         # Include other required fields in the request
    #     })

    #     self.assertRedirects(response, reverse('login'))
    #     self.assertEqual(response.status_code, 302)