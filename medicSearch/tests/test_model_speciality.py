from django.test import TestCase
from medicSearch.models import Speciality

class SpecialityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Speciality.objects.create(name='Test Speciality')

    def test_name_field(self):
        speciality = Speciality.objects.get(id=1)
        field_label = speciality._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        speciality = Speciality.objects.get(id=1)
        max_length = speciality._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_status_field_default_value(self):
        speciality = Speciality.objects.get(id=1)
        default_value = speciality._meta.get_field('status').default
        self.assertEqual(default_value, True)

    def test_created_at_auto_now_add(self):
        speciality = Speciality.objects.get(id=1)
        auto_now_add = speciality._meta.get_field('created_at').auto_now_add
        self.assertEqual(auto_now_add, True)

    def test_updated_at_auto_now(self):
        speciality = Speciality.objects.get(id=1)
        auto_now = speciality._meta.get_field('updated_at').auto_now
        self.assertEqual(auto_now, True)

    def test_str_method(self):
        speciality = Speciality.objects.get(id=1)
        expected_str = 'Test Speciality'
        self.assertEqual(str(speciality), expected_str)