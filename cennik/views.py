from django.shortcuts import render
from .models import Indywidualny
from .models import Naglowek


def indywidualny_list (request):
	queryset_naglowek = Naglowek.objects.all()
	queryset_indywidualny = Indywidualny.objects.all()
	context = {
		"indywidualny_list": queryset_indywidualny,
		"naglowek_list": queryset_naglowek,		
		"title": "View"
		}
	return render(request, 'cennik.html', context)