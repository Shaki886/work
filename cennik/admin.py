from django.contrib import admin

from .models import DNI
admin.site.register(DNI)

from .models import CENNIK_IND
admin.site.register(CENNIK_IND)

from .models import CENNIK_DEA
admin.site.register(CENNIK_DEA)

from .models import DODATKI
admin.site.register(DODATKI)