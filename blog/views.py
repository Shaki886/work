from django.shortcuts import render
from django.utils import timezone
from .models import Post

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    	
    return render(request, 'blog/blog.html', {'posts': posts})
	
class PostList(ListView):
    paginate_by = 4 #this variable is used for pagination 
    def get_queryset(self):
                 
        if 'search' in self.request.GET:
            objects = Post.objects.filter(
                Q(title__icontains=self.request.GET['search']) | Q(body__icontains=self.request.GET['search'])
                )
        else:
            objects = Post.objects.all()
         
        return objects