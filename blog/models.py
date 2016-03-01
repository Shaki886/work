from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=12)
    krotki_opis = models.CharField(max_length=25)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=300)
    height_field = models.IntegerField(default=380)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title