from datetime import date

from django import forms
from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.template.context import Context

from models import PersonalData


class PersonalDataForm(forms.ModelForm):

    class Meta:
        model = PersonalData

    def __init__(self, *args, **kwargs):
        kwargs['instance'] = PersonalData.objects.get(id=1)
        super(PersonalDataForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget = forms.widgets.Textarea()
        self.fields['other_contacts'].widget = forms.widgets.Textarea()
        self.fields['birthdate'].widget = DatepickerWidget()


class DatepickerWidget(Widget):

    def render(self, name, value, attrs=None):
        print 'value', value
        if isinstance(value, date):
            value = value.strftime('%m/%d/%Y')
        return render_to_string(
            'widgets/datepicker_widget.html', locals(), context_instance=Context(locals()))
