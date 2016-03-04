from django import forms
from django.db import models

class KontaktForm(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numer_ogloszenia = forms.IntegerField(required=True)
    telefon = forms.IntegerRangeField(min_value=9, max_value=12) 

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
	
	
	
	
	
