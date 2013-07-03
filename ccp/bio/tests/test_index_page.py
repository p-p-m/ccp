from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from bio.models import PersonalData
from bio.templatetags.admin_edit_tags import edit_link


class TestIndexPage(TestCase):

    mydata_fields = {
        'name': 'Pavel',
        'surname': 'Marchuk',
        'birthdate': datetime.strptime('02.01.1990', '%d.%m.%Y').date(),
        'bio': 'Ended NTUU KPI. Now working at plasticjam',
        'email': 'marchukpavelp@gmail.com',
        'skype': 'zim.inv',
        'other_contacts': '-',
        'jabber': 'pavel@khavr.com'
    }

    def test_personal_data_model(self):
        mydata = PersonalData.objects.get(id=1)
        for field, value in self.mydata_fields.items():
            self.assertEqual(getattr(mydata, field), value)

    def test_personal_data_on_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.mydata_fields['birthdate'] = 'Jan. 2, 1990'
        for field, value in self.mydata_fields.items():
            self.assertContains(response, field.title().replace('_', ' '))
            self.assertContains(response, value)

    def test_edit_link(self):
        adm = User.objects.get(id=1)
        self.assertEqual(edit_link(adm), '/admin/auth/user/1/')
