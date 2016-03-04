from django import forms
from django import models

class KontaktForm(forms.Form):
    INDYWIDUALNY = 'Indywidualny'
    DEALER = 'Dealer'
    RODZAJ_KLIENTA_CHOICES = (
        (INDYWIDUALNY, 'Indywidualny'),
        (DEALER, 'Dealer'),
        )
    Rodzaj_klienta = model.CharField(max_length=2,
                                      choices=RODZAJ_KLIENTA_CHOICES,
                                      default=INDYWIDUALNY)
    title = forms.CharField(required=True)
    text = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numer_ogloszenia = forms.IntegerField(required=True)
    telefon = forms.CharField(min_length=9) 
	
	

	
	
	
	
	
