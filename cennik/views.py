from django.shortcuts import render

from .models import DNI
from .models import CENNIK_IND
from .models import CENNIK_DEA
from .models import DODATKI

def cennik(request):

    cennik_ind = CENNIK_IND.objects.order_by()
    cennik_dea = CENNIK_DEA.objects.order_by()
    dodatki = DODATKI.objects.order_by()

    return render(request, 'cennik/cennik.html', {'cennik': cennik})
	
def dni(request):
	dni = DNI.objects.all()
	context = {
		"dni": queryset,
		"title": "Dni"
		}
	return render(request, "cennik.html", context)