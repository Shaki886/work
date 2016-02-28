from django.shortcuts import render

from .models import BLOG

def blog(request):

    blogs = BLOG.objects.order_by()

    return render(request, 'blog/blog.html', {'blogs': blogs})