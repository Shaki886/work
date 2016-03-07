from django.shortcuts import render
from .models import Indywidualny
from .models import Naglowek1
from .models import Naglowek2
from .models import Dealer
from .models import Dodatkowe


def indywidualny_list (request):
	queryset_naglowek1 = Naglowek1.objects.all()
	queryset_naglowek2 = Naglowek1.objects.all()
	queryset_indywidualny = Indywidualny.objects.all()
	queryset_dealer = Dealer.objects.all()
	queryset_dodatkowe = Dodatkowe.objects.all()
	context = {
		"indywidualny_list": queryset_indywidualny,
		"naglowek1_list": queryset_naglowek1,
		"naglowek2_list": queryset_naglowek2,		
		"dealer_list": queryset_dealer,
		"dodatkowe_list": queryset_dodatkowe,	
		"title": "View"
		}
	return render(request, 'cennik.html', context)