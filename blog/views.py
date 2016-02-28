from django.shortcuts import render
from .models import Blog

def Blog(request):

    blog = Blog.objects.order_by()

    return render(request, 'blog/blog.html', {'blogs': blogs})