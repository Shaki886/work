from django.views import generic


class Post(generic.ListView):
    paginate_by = 1
    context_object_name = 'post'

post = Post.as_view()