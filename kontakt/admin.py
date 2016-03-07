from django.contrib import admin

from .models import Kontakt
from .models import Temat

admin.site.register(Temat)
admin.site.register(Kontakt)