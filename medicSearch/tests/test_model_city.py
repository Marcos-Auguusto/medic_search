from django.test import TestCase
from medicSearch.models import City, State

class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        state = State.objects.create(name='Test State')
        City.objects.create(name='Test City', state=state)

    def test_city_str_representation(self):
        city = City.objects.get(name='Test City')
        expected_str = 'Test City - Test State'
        self.assertEqual(str(city), expected_str)

    def test_city_status_default_value(self):
        city = City.objects.get(name='Test City')
        self.assertTrue(city.status)

    def test_city_created_at_auto_now_add(self):
        city = City.objects.get(name='Test City')
        self.assertIsNotNone(city.created_at)

    def test_city_updated_at_auto_now(self):
        city = City.objects.get(name='Test City')
        self.assertIsNotNone(city.updated_at)

    def test_city_state_foreign_key(self):
        city = City.objects.get(name='Test City')
        self.assertIsInstance(city.state, State)
        self.assertEqual(city.state.name, 'Test State')