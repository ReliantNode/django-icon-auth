import string
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    signature = forms.CharField(widget=forms.HiddenInput, max_length=132)
    username = forms.CharField(widget=forms.HiddenInput, max_length=132)

    def __init__(self, token, *args, **kwargs):
        self.token = token
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_signature(self):
        sig = self.cleaned_data['signature']

        if len(sig) != 88:
            raise forms.ValidationError('Invalid signature')

        return sig
