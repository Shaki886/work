from django.shortcuts import render

def wiadomosciv2(request):
    return render(request, 'wiadomosciv2/wiadomosciv2.html', {})