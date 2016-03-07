from django.db import models

class Indywidualny(models.Model):
	numer_wiersza = models.CharField(max_length=10)
	kolumna_1 = models.CharField(max_length=100)
	kolumna_2 = models.CharField(max_length=100)
	kolumna_3 = models.CharField(max_length=100)
	kolumna_4 = models.CharField(max_length=100)

	
	def __str__(self):
		return self.numer_wiersza