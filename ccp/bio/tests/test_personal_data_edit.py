from datetime import datetime

from django.test import TestCase
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
        'email': 'marchukpavelp@gmail.com2',
        'skype': 'zim.inv2',
        'other_contacts': '-2',
        'jabber': 'pavel@khavr.com2'
    }

    pdurl = reverse('personal_data_update')

    def _user(self):
        return User.objects.create(
            username='artur', password='dent', email='artur@i.ua')

    def test_personal_data_form(self):
        form = PersonalDataForm(data=self.new_form_fields)
        self.assertTrue(form.is_valid)
        form.save()
        mydata = PersonalData.objects.get(id=1)
        for field, value in self.new_fields.items():
            self.assertEqual(getattr(mydata, field), value)

    def test_not_logged_request(self):
        ''' Testing request from not logged in user '''
        for method in 'get', 'post':
            response = getattr(self.client, method)(self.pdurl)
            # self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('login'))

    def test_logged_get_request(self):
        self.assertTrue(
            self.client.login(username='artur', password='dent'))
        response = self.client.get(self.pdurl)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        mydata = PersonalData.objects.get(id=1)
        for f in PersonalData._meta.fields:
            self.assertContains(response, getattr(mydata, f.name))
        # test photo on page:
        self.assertIn('myphoto', response.context)
        self.assertContains(response, 'img')

    def test_logged_post_request(self):
        self.assertTrue(
            self.client.login(username='artur', password='dent'))
        response = self.client.post(self.pdurl, data=self.new_form_fields)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'personal data were successfully saved')
        mydata = PersonalData.objects.get(id=1)
        for field, value in self.new_form_fields.items():
            self.assertEqual(getattr(mydata, field), value)

