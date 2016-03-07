from django.db import models

class Indywidualny(models.Model):
	numer_wiersza = models.IntegerField()
	wiersz = models.CharField(max_length=100)

	
	def __str__(self):
		return self.numer_wiersza