from django.shortcuts import render
from .models import Indywidualny
from .models import Naglowek

def naglowek_list (request):
	queryset = Naglowek.objects.all()
	context = {
		"naglowek_list": queryset,
		"title": "View"
		}
	return render(request, 'cennik.html', context)

def indywidualny_list (request):
	queryset = Indywidualny.objects.all()
	context = {
		"indywidualny_list": queryset,
		"title": "View"
		}
	return render(request, 'cennik.html', context)