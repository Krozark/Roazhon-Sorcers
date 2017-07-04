# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django import forms

class ContactForm (forms.Form):
    subject = forms.CharField(label=_('Sjet'),max_length =100)
    email_from = forms.EmailField(label=_('Mail'), max_length=250)
    message = forms.CharField(label=_('Message'),widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

