from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings


class TestSettingsContextProcessor(TestCase):

    def test_settings_in_context(self):
        response = self.client.get(reverse('index'))
        self.assertIn('settings', response.context)
        self.assertEqual(response.context['settings'], settings)
