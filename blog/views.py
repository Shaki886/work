from django.shortcuts import render
from .models import Post

def Post(request):

    posts= Post.objects.order_by()

    return render(request, 'blog/blog.html', {'posts': posts})