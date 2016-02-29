from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views import generic
from blog import models

class PostList(generic.ListView):
    model = models.Post
    paginate_by = 4
    context_object_name = 'post_list'

post_list = NewsList.as_view()