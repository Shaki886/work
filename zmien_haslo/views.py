from django.shortcuts import render

def zmien_haslo(request):
    return render(request, 'zmien_haslo/zmien_haslo.html', {})