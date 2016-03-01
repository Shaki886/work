from django import forms



class KontForm(forms.ModelForm):
    class Meta:
        exclude = ('views',)
        # fields = (...)