from django.test import TestCase
from medicSearch.models import Neighborhood, City


class NeighborhoodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        city = City.objects.create(name='Test City')
        Neighborhood.objects.create(name='Test Neighborhood', city=city)

    def test_neighborhood_str(self):
        neighborhood = Neighborhood.objects.get(name='Test Neighborhood')
        expected_str = 'Test Neighborhood - Test City'
        self.assertEqual(str(neighborhood), expected_str)

    def test_neighborhood_status_default(self):
        neighborhood = Neighborhood.objects.get(name='Test Neighborhood')
        self.assertTrue(neighborhood.status)

    def test_neighborhood_created_at(self):
        neighborhood = Neighborhood.objects.get(name='Test Neighborhood')
        self.assertIsNotNone(neighborhood.created_at)

    def test_neighborhood_updated_at(self):
        neighborhood = Neighborhood.objects.get(name='Test Neighborhood')
        self.assertIsNotNone(neighborhood.updated_at)
