from django.shortcuts import render

def dodaj_ogloszenie(request):
    return render(request, 'dodaj_ogloszenie/dodaj_ogloszenie.html', {})