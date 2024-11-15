from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data


class TestForm(forms.Form):
    bool = forms.BooleanField(required=False)
    nullbool = forms.NullBooleanField(label='非空布尔值')
    integer = forms.IntegerField(label='整数',label_suffix='===')
    float = forms.FloatField()
    decimal = forms.DecimalField()
    char = forms.CharField(initial='abc')
    choicelist = [
        ('a','asddd'),
        ('b','bsddd'),
        ('c','csddd'),
    ]
    choice = forms.ChoiceField(help_text='123',choices=choicelist)
    typedchoice = forms.TypedChoiceField()
    multiplechoice = forms.MultipleChoiceField()
    typedmultiplechoice = forms.TypedMultipleChoiceField()
    date = forms.DateField(disabled=True)
    time = forms.TimeField()
    datetime = forms.DateTimeField()
    duration = forms.DurationField()
    email = forms.EmailField()
    formTextInput = forms.CharField(widget=forms.TextInput)
    formNumberInput = forms.CharField(widget=forms.NumberInput)
    formEmailInput = forms.CharField(widget=forms.EmailInput)
    formURLInput = forms.CharField(widget=forms.URLInput)
    formPasswordInput = forms.CharField(widget=forms.PasswordInput)
    formHiddenInput = forms.CharField(widget=forms.HiddenInput)
    formDateInput = forms.CharField(widget=forms.DateInput)
    formTimeInput = forms.CharField(widget=forms.TimeInput)
    formDateTimeInput = forms.CharField(widget=forms.DateTimeInput)
    formTextarea = forms.CharField(widget=forms.Textarea)
    formCheckboxInput = forms.CharField(widget=forms.CheckboxInput)
    formSelect = forms.CharField(widget=forms.Select)