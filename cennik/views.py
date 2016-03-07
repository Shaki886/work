from django.shortcuts import render

def cennik(request):
    return render(request, 'cennik/cennik.html', {})