from django.shortcuts import render

def kontaktok(request):
    return render(request, 'kontaktok/kontaktok.html', {})