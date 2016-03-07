from django import forms
	
class KontaktForm(forms.ModelForm):
    class Meta:
        model = Kontakt