from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from django.core.mail import send_mail
from .forms import KontaktForm
from .models import Temat

def kontakt(request):
	form_class = KontaktForm
	temats= TEMAT.objects.order_by()

	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			klient = request.POST.get('klient')
			tytul = request.POST.get('tytul')
			tekst = request.POST.get('tekst')
			imie_i_nazwisko = request.POST.get('imie_i_nazwisko')
			email = request.POST.get('email')
			numer_ogloszenia = request.POST.get('numer_ogloszenia')
			telefon = request.POST.get('telefon')
			send_mail('Subject here', tekst, email, ['shaki886@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/kontaktok/')
	return render(request, 'kontakt/kontakt.html', {'form': form})



def temat(request):


    return (request, '', {'temats': temats})


