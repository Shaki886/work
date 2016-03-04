from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = models.Post
    paginate_by = 4
    context_object_name = 'post_list'

post_list = PostList.as_view()

def post_view(request):
	queryset = Post.objects.all()
	context_data = {
		"object_list": queryset,
		"title": "View"
	}
	return render(request, "view.html", context)