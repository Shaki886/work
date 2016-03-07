from django.contrib import admin
from .models import Indywidualny
from .models import Naglowek1
from .models import Naglowek2
from .models import Dealer
from .models import Dodatkowe

admin.site.register(Indywidualny)
admin.site.register(Naglowek1)
admin.site.register(Naglowek2)
admin.site.register(Dealer)
admin.site.register(Dodatkowe)