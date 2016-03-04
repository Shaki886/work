from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Post


def post_list(request):
	queryset = Post.objects.all()
	context = {
		"post_list": queryset,
		"title": "View"
		}
	return render(request, "post_list.html", context)
	
def post_view(request):
	instance = get_object_or_404(Post, id=3)
	context = {
		"title": "Detail",
		"instance": instance,
		}
	return render(request, "view.html", context)