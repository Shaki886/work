from django.db import models
from django.utils import timezone

class Kategorie_aut(models.Model):
	nazwa_kategorii = models.CharField(max_length=200)

	def __str__(self):
		return self.nazwa_kategorii


	def content_file_name(instance, filename):
		return '/files/'.join(['content', instance.user.username, filename])
class Post(models.Model):
	Login = models.ForeignKey('auth.User')
	kategoria = models.ForeignKey(Kategorie_aut)
	Tytul = models.CharField(max_length=200)
	Marka = models.TextField(50)
	Model = models.TextField(50)
	Rok = models.IntegerField(4)
	Stan = Nowy || Uzywany
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