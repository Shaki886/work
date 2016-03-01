from django.shortcuts import render

from .models import POMOC

def pomoc(request):

    pomocs= POMOC.objects.order_by()

    return render(request, 'pomoc/pomoc.html', {'pomocs': pomocs})