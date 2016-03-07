from django.shortcuts import render
from .models import Indywidualny
from .models import Naglowek1
from .models import Dealer


def indywidualny_list (request):
	queryset_naglowek1 = Naglowek1.objects.all()
	queryset_indywidualny = Indywidualny.objects.all()
	queryset_dealer = Dealer.objects.all()
	context = {
		"indywidualny_list": queryset_indywidualny,
		"naglowek1_list": queryset_naglowek1,	
		"dealer_list": queryset_dealer,	
		"title": "View"
		}
	return render(request, 'cennik.html', context)