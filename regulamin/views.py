from django.shortcuts import render

def regulamin(request):
    return render(request, 'regulamin/regulamin.html', {})