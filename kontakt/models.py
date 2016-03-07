# -*- coding: utf-8 -*-
from django.db import models

class KontaktForm(models.Model):
    klient = models.CharField(required=False)
    tytul = models.CharField(required=False)
    tekst = models.CharField(
        required=True,
        widget=models.Textarea
    )
    imie_i_nazwisko = models.CharField(required=True)
    email = models.EmailField(required=True)
    numer_ogloszenia = models.CharField(required=True)
    telefon = models.CharField(min_length=9)

class Temat(models.Model):
	temat = models.CharField(max_length=100)
	
	def __str__(self):
		return self.temat