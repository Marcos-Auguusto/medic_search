from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class HomePatientViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_patient_url = reverse('home_patient')

    def test_home_patient_view_with_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        response = self.client.get(self.home_patient_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homePatient.html')

    def test_home_patient_view_without_authenticated_user(self):
        response = self.client.get(self.home_patient_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login-patient/?next=/home-patient')