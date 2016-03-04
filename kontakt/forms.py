from django import forms

class KontaktForm(forms.Form):
    INDYWIDUALNY = 'Indywidualny'
    DEALER = 'Dealer'
    RODZAJ_KLIENTA_CHOICES = (
        (INDYWIDUALNY, 'Indywidualny'),
        (DEALER, 'Dealer'),
        )
    Rodzaj_klienta= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                  choices=RODZAJ_KLIENTA_CHOICES)
    Tytuł = forms.CharField(required=True)
    Tekst = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    Imię_i_Nazwisko = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Numer_ogłoszenia = forms.IntegerField(required=True)
    Telefon = forms.CharField(min_length=9) 

	
	
	
	
