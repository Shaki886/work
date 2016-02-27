# -*- coding: utf-8 -*-
from django.db import models

class FAQ(models.Model):
	autor = models.ForeignKey('auth.User')
	tytul = models.CharField(max_length=200)
	tresc = models.TextField()
	
	
	
	def __str__(self):
		return self.tytul