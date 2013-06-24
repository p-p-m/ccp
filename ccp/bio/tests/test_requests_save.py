from django.test import TestCase
from django.core.urlresolvers import reverse

from bio.models import Request


class TestRequestsInDB(TestCase):

    request_stored_fields = ('META', 'body', 'path')

    def test_request_storage(self):
        response = self.client.get(reverse('index'))
        stored_request = Request.objects.latest()
        for at in self.request_stored_fields:
            stored = getattr(stored_request, at.lower())
            sent = getattr(response.request, at)
            self.assertEqual(stored, sent)

    def test_requets_page(self):
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        for at in self.request_stored_fields:
            self.assertContains(response, getattr(response.request, at))
