from django.views import generic
from blog import models




class OneList(generic.ListView):
    model = models.Post
    paginate_by = 1
    context_object_name = 'one_list'
    template_name = 'one_list.html'