# -*- coding: utf-8 -*-
from django.db import models

class Temat(models.Model):
	temat = models.CharField(max_length=100)
	
	def __str__(self):
		return self.temat