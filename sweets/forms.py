from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-field'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'field'}))
