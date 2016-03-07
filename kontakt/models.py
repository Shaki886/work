# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class KontaktForm(models.Model):
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

class Temat(models.Model):
	temat = models.CharField(max_length=100)
	
	def __str__(self):
		return self.temat