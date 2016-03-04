from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from blog import models

class PostList(generic.ListView):
    model = models.Post
    paginate_by = 4
    context_object_name = 'post_list'

post_list = PostList.as_view()

def post_view(request):
	return render(request, "view.html", {})