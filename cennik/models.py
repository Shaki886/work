from django.db import models

class Indywidualny(models.model):
	numer_wiersza = models.IntegerField()
	wiersz = models.CharField(max_length=100)
