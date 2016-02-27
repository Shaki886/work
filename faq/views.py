from django.shortcuts import render

from .models import FAQ

def faq(request):

    faqs= FAQ.objects.order_by()

    return render(request, 'faq/faq.html', {'faqs': faqs})