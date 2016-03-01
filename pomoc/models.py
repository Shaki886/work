# -*- coding: utf-8 -*-
from django.db import models

class POMOC(models.Model):
	numer = models.IntegerField()
	tytul = models.CharField(max_length=200)
	tresc = models.TextField()
	
	
	
	def __str__(self):
		return self.tytul