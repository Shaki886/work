from django.contrib import admin

from .models import KontaktForm
from .models import Temat

admin.site.register(Temat)
admin.site.register(KontaktForm)