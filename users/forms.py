# _*_ coding: utf-8 _*_
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import FormularzLogowania

class FormularzLogowania(forms.Form):
    email = forms.CharField(label="email:",max_length=30)
    password = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    def clean_eamil(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            return email
        except ObjectDoesNotExist:
            raise forms.ValidationError("Niepoprawny email")        
    def clean_password(self):
        if self.cleaned_data.has_key('email'):
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            user = User.objects.get(email=email)
            if user.check_password(password):
                return password
            raise forms.ValidationError("Niepoprawne hasło")                
        raise forms.ValidationError("Niepoprawny email")