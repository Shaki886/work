from django.shortcuts import render

def pomoc(request):
    return render(request, 'pomoc/pomoc.html', {})