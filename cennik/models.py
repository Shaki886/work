# -*- coding: utf-8 -*-
from django.db import models

class DNI(models.Model):
	kolumna1 =models.CharField(max_length=200)
	kolumna2 =models.CharField(max_length=200)
	kolumna3 =models.CharField(max_length=200)
	
class CENNIK_IND(models.Model):
	szczegoly = models.CharField(max_length=200)
	kolumna1 =models.CharField(max_length=200)
	kolumna2 =models.CharField(max_length=200)
	kolumna3 =models.CharField(max_length=200)
	
class CENNIK_DEA(models.Model):
	kolumna1 =models.CharField(max_length=200)
	kolumna2 =models.CharField(max_length=200)
	
class DODATKI(models.Model):
	dodatki = models.CharField(max_length=500)
