from django import forms

class KontaktForm(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numer_ogloszenia = forms.IntegerField(required=True)
    telefon = forms.IntegerField() 
	
	
	
	
	
	
	
	
	
