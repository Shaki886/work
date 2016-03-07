from django import forms

class KontaktForm(forms.Form):
    klient = forms.CharField(required=False)
    tytul = forms.CharField(required=False)
    tekst = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    imie_i_nazwisko = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numer_ogloszenia = forms.CharField(required=True)
    telefon = forms.CharField(min_length=9)