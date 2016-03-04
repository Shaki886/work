from django import forms

class KontaktForm(forms.Form):
	email = forms.EmailField()
	title = forms.CharField()
	text = forms.Charfield( widget=forms.Textarea)


	
	
	
	
	
	
	
