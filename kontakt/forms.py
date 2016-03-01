from django import forms

from kontakt.models import Kontakt


class KontForm(forms.ModelForm):
    class Meta:
        model = Kontakt
        exclude = ('views',)
        # fields = (...)