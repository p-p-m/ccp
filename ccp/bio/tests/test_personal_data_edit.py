import os
import uuid
from datetime import datetime

from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from bio.forms import PersonalDataForm
from bio.models import PersonalData


class TestIndexPage(TestCase):

    new_form_fields = {
        'name': 'Pavel2',
        'surname': 'Marchuk2',
        'birthdate': datetime.strptime('02.02.1990', '%d.%m.%Y').date(),
        'bio': 'Ended NTUU KPI. Now working at plasticjam2',
        'email': 'marchukpavelp2@gmail.com',
        'skype': 'zim.inv2',
        'other_contacts': '-2',
        'jabber': 'pavel@khavr.com2',
    }

    pdurl = reverse('personal_data_update')

    def _login_user(self):
        User.objects.create_user(
            username='artur', password='dent', email='artur@i.ua')
        self.assertTrue(
            self.client.login(username='artur', password='dent'))

    def test_personal_data_form(self):
        form = PersonalDataForm(data=self.new_form_fields)
        form.is_valid()
        self.assertTrue(form.is_valid())

        form.save()
        mydata = PersonalData.objects.get(id=1)
        for field, value in self.new_form_fields.items():
            self.assertEqual(getattr(mydata, field), value)

    def test_not_logged_request(self):
        ''' Testing request from not logged in user '''
        for method in 'get', 'post':
            response = getattr(self.client, method)(self.pdurl)
            self.assertRedirects(response, reverse('login') + '?next=/personal-data/update/')

    def test_logged_get_request(self):
        self._login_user()
        response = self.client.get(
            self.pdurl, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        mydata = PersonalData.objects.get(id=1)
        for f in PersonalData._meta.fields:
            self.assertContains(response, getattr(mydata, f.name))

    def test_logged_post_request(self):
        self._login_user()
        response = self.client.post(self.pdurl, data=self.new_form_fields)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Personal data were successfully saved')
        mydata = PersonalData.objects.get(id=1)
        for field, value in self.new_form_fields.items():
            self.assertEqual(getattr(mydata, field), value)

    def test_change_photo_request(self):
        self._login_user()
        # creating file:
        f = open(str(uuid.uuid4()) + '.jpeg', 'w+')
        f.write('test_image')
        f.close()
        # testing file:
        f = open(f.name, 'r+')
        self.new_form_fields['photo'] = f
        response = self.client.post(self.pdurl, data=self.new_form_fields)
        self.assertEqual(response.status_code, 200)
        mydata = PersonalData.objects.get(id=1)
        self.assertEqual(mydata.photo, 'myphoto/' + os.path.basename(f.name))
        del self.new_form_fields['photo']
        f.close()
        os.remove(f.name)
        os.remove(os.path.join(settings.MEDIA_ROOT, 'myphoto', os.path.basename(f.name)))
