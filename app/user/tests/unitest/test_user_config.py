from django.apps import apps
from django.test import TestCase
from user.apps import UserConfig


class UserConfigTest(TestCase):
    """
    Testing apps.py in django
    Test to cover apps.py files for user model

    Source:
    https://stackoverflow.com/questions/
    43334953/testing-apps-py-in-django
    """

    def test_apps_user(self):
        self.assertEqual(UserConfig.name, 'user')
        self.assertEqual(apps.get_app_config('user').name, 'user')
