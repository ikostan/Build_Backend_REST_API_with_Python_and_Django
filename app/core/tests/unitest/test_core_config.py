from django.apps import apps
from django.test import TestCase
from core.apps import CoreConfig


class CoreConfigTest(TestCase):
    """
    Testing apps.py in django
    Test to cover apps.py files for core model

    Source:
    https://stackoverflow.com/questions/
    43334953/testing-apps-py-in-django
    """

    def test_apps_core(self):
        self.assertEqual(CoreConfig.name, 'core')
        self.assertEqual(apps.get_app_config('core').name, 'core')
