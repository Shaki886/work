from django.shortcuts import render

def danedo_faktury(request):
    return render(request, 'danedo_faktury/danedo_faktury.html', {})