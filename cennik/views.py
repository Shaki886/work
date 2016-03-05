from django.shortcuts import render

from .models import DNI
from .models import CENNIK_IND
from .models import CENNIK_DEA
from .models import DODATKI

	
def dni_list(request):
	queryset_list = DNI.objects.all()
	context = {
		"dni_list": queryset,
		"title": "View"
		}
	return render(request, "cennik.html", context)
	
def cenni_ind_list(request):
	queryset_list = CENNIK_IND.objects.all()
	context = {
		"cenni_ind": queryset,
		"title": "View"
		}
	return render(request, "cennik.html", context)
	
def cennik_dea_list(request):
	queryset_list = CENNIK_DEA.objects.all()
	context = {
		"cenni_dea": queryset,
		"title": "View"
		}
	return render(request, "cennik.html", context)
	
def dodatki_list(request):
	queryset_list = DODATKI.objects.all()
	context = {
		"dodatki_list": queryset,
		"title": "View"
		}
	return render(request, "cennik.html", context)