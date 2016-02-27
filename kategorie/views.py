from django.shortcuts import render

def kategorie(request):
    return render(request, 'kategorie/kategorie.html', {})