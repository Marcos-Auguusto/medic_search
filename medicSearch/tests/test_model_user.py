from django.test import TestCase
from django.contrib.auth.models import User
<<<<<<< HEAD


class UserModelTestClass(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='test')
    
    def test_user_exist(self):
        user = User.objects.first()
        self.assertIsNotNone(user)
=======
from medicSearch.models import Profile


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user, created = User.objects.get_or_create(username='testuser')
        if created:
            test_user.set_password('12345')
            test_user.save()
        Profile.objects.get_or_create(user=test_user)

    def test_profile_creation(self):
        user = User.objects.get(username='testuser')
        self.assertIsInstance(user.profile, Profile)

    def test_profile_update(self):
        user = User.objects.get(username='testuser')
        user.profile.role = 2
        user.profile.save()
        self.assertEqual(user.profile.role, 2)
>>>>>>> 150a09b291a41e61e4ae17ab4fa027b875e9f601
