from django.views import generic
from blog import models

class PostList(generic.ListView):
    model = models.Post
    paginate_by = 4
    context_object_name = 'post_list'
    template_name = 'post_list.html'


class ViewList(generic.ListView):
    model = models.Post
    paginate_by = 1
    context_object_name = 'view_list'
    template_name = 'view_list.html'