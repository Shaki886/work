from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Post


def post_view(request):
	queryset = Post.objects.all()
	context = {
		"post_list": queryset,
		"title": "View"
		}
	return render(request, "view.html", context)
	
	