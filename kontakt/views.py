from django.shortcuts import render

from kontakt.forms import KontaktForm

def kontakt(request):
    return render(request, 'kontakt/kontakt.html', {})