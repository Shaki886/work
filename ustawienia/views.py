from django.shortcuts import render

def ustawienia(request):
    return render(request, 'ustawienia/ustawienia.html', {})