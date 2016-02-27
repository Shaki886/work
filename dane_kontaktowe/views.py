from django.shortcuts import render

def dane_kontaktowe(request):
    return render(request, 'dane_kontaktowe/dane_kontaktowe.html', {})