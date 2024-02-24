from django.test import TestCase
from medicSearch.models import State

class StateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        State.objects.create(name='State 1')

    def test_state_creation(self):
        state = State.objects.get(name='State 1')
        self.assertEqual(state.name, 'State 1')
        self.assertTrue(state.status)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    def test_state_str_representation(self):
        state = State.objects.get(name='State 1')
        self.assertEqual(str(state), 'State 1')