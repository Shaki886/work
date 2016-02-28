from django.db import models
from django.utils import timezone

class BLOG(models.Model):
	Login = models.ForeignKey('auth.User')
	Tytul = models.CharField(max_length=200)
	Marka = models.CharField(max_length=50)
	Model = models.CharField(max_length=50)
	Rok = models.IntegerField(4)
	Stan = models.TextField(default='uzywany')
	Przebieg = models.IntegerField(50)
	zdjecie = models.FileField()
	Opis = models.TextField(500)
	data_utworzenia = models.DateTimeField(default=timezone.now)
	data_publikacji = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.data_publikacji = timezone.now()
		self.save()

	def __str__(self):
		return self.tytul
		
	def __unicode__(self):
		return self.filename