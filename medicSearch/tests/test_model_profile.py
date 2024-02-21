from django.test import TestCase
from django.contrib.auth.models import User
from medicSearch.models import Profile, Rating


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user, created = User.objects.get_or_create(username='testuser')
        if created:
            test_user.set_password('12345')
            test_user.save()
        Profile.objects.get_or_create(user=test_user)

        test_user_rated, created = User.objects.get_or_create(
            username='testuser_rated')
        if created:
            test_user_rated.set_password('12345')
            test_user_rated.save()
        Profile.objects.get_or_create(user=test_user_rated)

    def test_profile_creation(self):
        user = User.objects.get(username='testuser')
        self.assertIsInstance(user.profile, Profile)

    def test_profile_update(self):
        user = User.objects.get(username='testuser')
        user.profile.role = 2
        user.profile.save()
        self.assertEqual(user.profile.role, 2)

    def test_show_scoring_average_with_ratings(self):
        user = User.objects.get(username='testuser')
        user_rated = User.objects.get(username='testuser_rated')
        Rating.objects.create(user=user, user_rated=user_rated, value=4)
        Rating.objects.create(user=user, user_rated=user_rated, value=5)
        profile = user_rated.profile
        self.assertEqual(profile.show_scoring_average(), 4.5)

    def test_show_scoring_average_without_ratings(self):
        user = User.objects.get(username='testuser')
        profile = user.profile
        self.assertEqual(profile.show_scoring_average(), 'Sem avaliações')

    def test_show_favorites(self):
        user = User.objects.get(username='testuser')
        profile = user.profile
        self.assertEqual(profile.show_favorites().count(), 0)

    def test_show_ratings(self):
        user = User.objects.get(username='testuser')
        profile = user.profile
        self.assertEqual(profile.show_ratings().count(), 0)
