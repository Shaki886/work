from django.shortcuts import render

def rejestracja_indywidualny(request):
    return render(request, 'rejestracja_indywidualny/rejestracja_indywidualny.html', {})