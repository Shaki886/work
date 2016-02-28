from django.shortcuts import render
from .models import BLOG

def Blog(request):

    blog = BLOG.objects.order_by()

    return render(request, 'blog/blog.html', {'blogs': blogs})