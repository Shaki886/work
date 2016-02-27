from django.shortcuts import render

def pojedynczy_wpis(request):
    return render(request, 'pojedynczy_wpis/pojedynczy_wpis.html', {})