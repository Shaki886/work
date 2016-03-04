from django import forms

class KontaktForm(forms.Form):

	tresc = forms.Charfield( widget=forms.Textarea)

	e-mail = forms.EmailField()

	
	
	
	
	
	
	
