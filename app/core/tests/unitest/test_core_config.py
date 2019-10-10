from django.apps import apps
from django.test import TestCase
from core.apps import CoreConfig


class CoreConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(CoreConfig.name, 'core')
        self.assertEqual(apps.get_app_config('core').name, 'core')
