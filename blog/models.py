from django.db import models
from django.utils import timezone

def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %{instance.id, filename.id, extension}

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
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