from django.test import TestCase
from django.utils.html import escape
from django.core.urlresolvers import reverse

from bio.models import Request


class TestRequestsInDB(TestCase):

    def test_request_storage(self):
        response = self.client.get(reverse('index'))
        stored_request = Request.objects.latest()
        for at in ('REQUEST_METHOD', 'PATH_INFO', 'CONTENT_TYPE', 'QUERY_STRING'):
            self.assertIn(at, stored_request.meta)
            self.assertIn(response.request[at], stored_request.meta)
        self.assertEqual(stored_request.path, response.request['PATH_INFO'])

    def test_requets_page(self):
        for i in range(11):
            response = self.client.get(reverse('stored_requests'))
            self.assertEqual(response.status_code, 200)
            for at in ('REQUEST_METHOD', 'PATH_INFO', 'CONTENT_TYPE', 'QUERY_STRING'):
                self.assertContains(response, response.request[at])

        first_requests = Request.objects.order_by('date_added')[:10]
        for req in first_requests:
            for attr in ('meta', 'path', 'priority'):
                self.assertContains(response, escape(getattr(req, attr)))
