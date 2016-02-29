from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	
    paginator  Paginator(entries, 4)
    page = paginator.page(1)
	
    ctx = {'page' : page }
	
    return render(request, 'blog/blog.html', {'posts': posts})