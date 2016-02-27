from django.shortcuts import render

def logowanie(request):
    return render(request, 'logowanie/logowanie.html', {})