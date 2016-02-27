from django.shortcuts import render

def wiadomosci(request):
    return render(request, 'wiadomosci/wiadomosci.html', {})