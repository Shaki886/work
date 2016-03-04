from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Post


def post_list(request):
	queryset_list = Post.objects.all().order_by("-created_date")
	paginator = Paginator(queryset_list, 4) 
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
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