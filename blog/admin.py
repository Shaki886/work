from django.contrib import admin

from .models import Kategorie_aut
from .models import Post
admin.site.register(Kategorie_aut)
admin.site.register(Post)