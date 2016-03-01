from django import forms



class KontForm(forms.ModelForm):
    class Meta:
        model = Kontakt
        exclude = ('views',)
        # fields = (...)