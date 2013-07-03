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
        # making 20 requests:
        for i in range(20):
            response = self.client.get(reverse('stored_requests'))

        # getting first 10 request from base and testing that they are at the page:
        first_requests = Request.objects.order_by('date_added')[:10]
        for req in first_requests:
            for attr in ('meta', 'path', 'priority'):
                self.assertContains(response, escape(getattr(req, attr)))

        # testing that only first ten request moves to page:
        for req1, req2 in zip(response.context['stored_requests'], first_requests):
            self.assertEqual(req1.date_added, req2.date_added)
