from django.contrib import admin

from .models import Kategorie_artykulu
from .models import Post
admin.site.register(Kategorie_artykulu)
admin.site.register(Post)