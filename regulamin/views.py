from django.shortcuts import render

from .models import REGULAMIN

def regulamin(request):

    regulamins= REGULAMIN.objects.order_by()

    return render(request, 'regulamin/regulamin.html', {'regulamins': regulamins})