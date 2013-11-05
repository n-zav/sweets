from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'class': 'special', 'text-align': 'center'}))
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={'size': '40'}))
    email = forms.EmailField()
