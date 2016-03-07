# -*- coding: utf-8 -*-
from django.db import models
		
class Temat(models.Model):
	temat = models.CharField(max_length=100)
	
	def __str__(self):
		return self.temat
		
class Kontakt(models.Model):
    klient = models.CharField(max_length=30)
    tytul = models.CharField(max_length=30)
    tekst = models.TextField()
    imie_i_nazwisko = models.CharField(max_length=60)
    email = models.EmailField()
    numer_ogloszenia = models.CharField(max_length=30)
    telefon = models.CharField(max_length=9)