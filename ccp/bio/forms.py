from django import forms

from models import PersonalData


class PersonalDataForm(forms.ModelForm):

    class Meta:
        model = PersonalData

    def __init__(self, *args, **kwargs):
        kwargs['instance'] = PersonalData.objects.get(id=1)
        super(PersonalDataForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget = forms.widgets.Textarea()
        self.fields['other_contacts'].widget = forms.widgets.Textarea()
