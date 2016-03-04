from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Post


def post_list(request):
	queryset = Post.objects.all().order_by("-timestamp")
	context = {
		"post_list": queryset,
		"title": "View"
		}
	return render(request, "post_list.html", context)
	
def post_view(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
		}
	return render(request, "view.html", context)