from django.shortcuts import render

def ogloszenie_widok(request):
    return render(request, 'ogloszenie_widok/ogloszenie_widok.html', {})