from django.shortcuts import render

def rejestracja_dealer(request):
    return render(request, 'rejestracja_dealer/rejestracja_dealer.html', {})