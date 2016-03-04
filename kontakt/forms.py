from django import forms

class KontaktForm(forms.Form):
    klient = forms.CharField(required=True)
    tytul = forms.CharField(required=True)
    tekst = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    imie_i_nazwisko = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numer_ogloszenia = forms.IntegerField(required=True)
    telefon = forms.CharField(min_length=9) 

	
	
	
	
