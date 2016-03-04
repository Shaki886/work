# -*- coding: utf-8 -*-
from django.db import models

class TEMAT(models.Model):
	temat = models.CharField(max_length=200)
	
	def __str__(self):
		return self.temat