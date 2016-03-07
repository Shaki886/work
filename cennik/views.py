from django.shortcuts import render
from .models import Indywidualny

def cennik(request):
    indywidualnys = Indywidualny.objects.filter
    return render(request, 'cennik/cennik.html', {})