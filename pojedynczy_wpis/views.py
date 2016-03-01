from django.views import generic
from pojedynczy_wpis import models

class Post(generic.ListView):
    model = models.Post
    paginate_by = 1
    context_object_name = 'post'

post = Post.as_view()