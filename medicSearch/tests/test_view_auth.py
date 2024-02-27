from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from medicSearch.models import Profile


class AuthViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login_patient')
        self.home_url = reverse('home_patient')

        self.patient_user = User.objects.create_user(
            username='patient',
            password='password'
        )

    def test_login_patient_view_authenticated_user(self):
        self.client.login(username='patient', password='password')

        response = self.client.get(self.login_url)

        self.assertRedirects(response, self.home_url)

    def test_login_patient_view_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'invalid',
            'password': 'invalid'
        }, follow=True)

        self.assertRedirects(response, self.login_url)

        self.assertContains(response, 'Usuário ou senha incorretos')

    def test_login_patient_view_valid_credentials_patient(self):
        response = self.client.post(self.login_url, {
            'username': 'patient',
            'password': 'password'
        })

        self.assertRedirects(response, self.home_url)

    def test_login_patient_view_missing_fields(self):
        response = self.client.post(self.login_url, {
            'username': 'patient'
        }, follow=True)

        self.assertRedirects(response, self.login_url)

        self.assertContains(
            response, 'Por favor, preencha todos os campos corretamente.')
