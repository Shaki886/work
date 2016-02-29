from django.shortcuts import render
from django.utils import timezone
from .models import Post

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginate_by = 4	
    return render(request, 'blog/blog.html', {'posts': posts})