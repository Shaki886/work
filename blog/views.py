from blog import models
from django.views.generic.edit import CreateView

class PostList(CreateView):
    model = models.Post
    paginate_by = 4
    context_object_name = 'post_list'
    template_name = 'post_list.html'


class ViewList(CreateView):
    model = models.Post
    paginate_by = 1
    context_object_name = 'view_list'
    template_name = 'view_list.html'