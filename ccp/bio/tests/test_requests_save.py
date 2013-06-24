from django.test import TestCase
from django.core.urlresolvers import reverse

from bio.models import Request


class TestRequestsInDB(TestCase):

    request_stored_fields = ('META', 'body', 'path')

    def test_request_storage(self):
        response = self.client.get(reverse('index'))
        stored_request = Request.objects.latest()
        print response.request
        for at in ('REQUEST_METHOD', 'PATH_INFO', 'CONTENT_TYPE', 'QUERY_STRING'):
            field = ':'.join([at, response.request[at]])
            self.assertIn(stored_request.meta, field)
        self.assertEqual(stored_request.path, response.request['PATH_INFO'])

    def test_requets_page(self):
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        for at in self.request_stored_fields:
            self.assertContains(response, getattr(response.request, at))
