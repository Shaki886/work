from django import forms
from .models import Kontakt
class KontaktForm(forms.ModelForm):
    class Meta:
        model = Kontakt
		fields = ('klient', 'tytul', 'tekst', 'imie_i_nazwisko', 'email', 'numer_ogloszenia', 'telefon')