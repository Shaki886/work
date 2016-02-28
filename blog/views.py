from django.shortcuts import render
from .models import Blog

def blog(request):

    blog= blog.objects.order_by()

    return render(request, 'blog/blog.html', {'blog': blog})