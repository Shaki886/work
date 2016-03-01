from django.views import generic
from blog import models

class PostList(generic.ListView):
    model = models.Post
    paginate_by = 1
    context_object_name = 'post_list'

post_list = PostList.as_view()