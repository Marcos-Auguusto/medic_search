from django.test import TestCase
from medicSearch.models import DayWeek

class DayWeekModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DayWeek.objects.create(name='Monday')

    def test_name_field(self):
        day_week = DayWeek.objects.get(id=1)
        field_label = day_week._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        day_week = DayWeek.objects.get(id=1)
        max_length = day_week._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_status_field(self):
        day_week = DayWeek.objects.get(id=1)
        field_label = day_week._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_status_default_value(self):
        day_week = DayWeek.objects.get(id=1)
        default_value = day_week._meta.get_field('status').default
        self.assertEqual(default_value, True)

    def test_created_at_field(self):
        day_week = DayWeek.objects.get(id=1)
        field_label = day_week._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_updated_at_field(self):
        day_week = DayWeek.objects.get(id=1)
        field_label = day_week._meta.get_field('updated_at').verbose_name
        self.assertEqual(field_label, 'updated at')

    def test_str_method(self):
        day_week = DayWeek.objects.get(id=1)
        expected_str = 'Monday'
        self.assertEqual(str(day_week), expected_str)