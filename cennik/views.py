from django.shortcuts import render
from .models import Indywidualny
from .models import IndywidualnyNaglowek

def indywidualny_list (request):
	queryset = Indywidualny.objects.all()
	context = {
		"indywidualny_list": queryset,
		"title": "View"
		}
	return render(request, 'cennik.html', context)
	
def indywidualnynaglowek_list (request):
	queryset = IndywidualnyNaglowek.objects.all()
	context = {
		"indywidualnynaglowek_list": queryset,
		"title": "View"
		}
	return render(request, 'cennik.html', context)