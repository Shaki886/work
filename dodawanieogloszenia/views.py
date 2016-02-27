from django.shortcuts import render

def dodawanieogloszenia(request):
    return render(request, 'dodawanieogloszenia/dodawanieogloszenia.html', {})