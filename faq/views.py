from django.shortcuts import render

from .models import FAQ

def faq(request):

    faq= FAQ.objects.order_by()

    return render(request, 'faq/faq.html', {'faq': faq})