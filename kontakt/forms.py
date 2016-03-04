from django import forms

class KontaktForm(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
	
	
	
	
	
	
	
