from django.shortcuts import render

from .models import Regulamin

def regulamin(request):

    regulamins= Regulamin.objects.order_by()

    return render(request, 'regulamin/regulamin.html', {'regulamins': regulamins})