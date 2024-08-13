from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from medicSearch.models import Profile

class MedicViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_medics_url = reverse('medics')

        user = User.objects.create_user(username='testuser', password='testpassword')

        self.profile, created = Profile.objects.get_or_create(user=user, defaults={'role': 2})

        if not created:
            self.profile.role = 2
            self.profile.save()

    def test_list_medics_view_with_filters(self):
        filters = {
            'name': 'John',
            'speciality': '1',
            'neighborhood': '2',
            'city': '3',
            'state': '4'
        }
        response = self.client.get(self.list_medics_url, filters)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['medics'],
            Profile.objects.filter(
                role=2,
                user__first_name__contains='John',
                specialties__id='1',
                addresses__neighborhood__id='2',
                addresses__neighborhood__city__id='3',
                addresses__neighborhood__city__state__id='4'
            ),
            transform=lambda x: x
        )

    def test_list_medics_view_without_filters(self):
        response = self.client.get(self.list_medics_url)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['medics'],
            Profile.objects.filter(role=2),
            transform=lambda x: x
        )