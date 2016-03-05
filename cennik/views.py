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
	
def dni_list(request):
	queryset_list = DNI.objects.all().order_by("-created_date")
	context = {
		"dni_list": queryset,
		"title": "View"
		}
	return render(request, "cennik.html", context)