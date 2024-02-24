from django.test import TestCase
from medicSearch.models import Address, Neighborhood, DayWeek

class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        neighborhood = Neighborhood.objects.create(name='Test Neighborhood')
        day_week = DayWeek.objects.create(name='Monday')
        Address.objects.create(
            neighborhood=neighborhood,
            name='Test Address',
            address='123 Test Street',
            latitude=0.0,
            longitude=0.0,
            opening_time='08:00:00',
            closing_time='18:00:00',
            phone='1234567890',
            status=True
        ).days_week.add(day_week)

    def test_address_str(self):
        address = Address.objects.get(name='Test Address')
        self.assertEqual(str(address), 'Test Address')

    def test_address_neighborhood(self):
        address = Address.objects.get(name='Test Address')
        self.assertEqual(address.neighborhood.name, 'Test Neighborhood')

    def test_address_days_week(self):
        address = Address.objects.get(name='Test Address')
        self.assertEqual(address.days_week.count(), 1)

    def test_address_status(self):
        address = Address.objects.get(name='Test Address')
        self.assertTrue(address.status)