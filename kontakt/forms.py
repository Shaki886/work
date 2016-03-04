from django import forms

class KontaktForm(forms.Form):
	e-mail = forms.EmailField()
	title = forms.CharField()
	text = forms.Charfield( widget=forms.Textarea)


	
	
	
	
	
	
	
