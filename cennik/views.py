from django.shortcuts import render
from .models import Indywidualny
from .models import NaglowekIndywidualny


def indywidualny_list (request):
	queryset_naglowek1 = NaglowekIndywidualny.objects.all()
	queryset_indywidualny = Indywidualny.objects.all()
	context = {
		"indywidualny_list": queryset_indywidualny,
		"naglowek1_list": queryset_naglowek1,		
		"title": "View"
		}
	return render(request, 'cennik.html', context)