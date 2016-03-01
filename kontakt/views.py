from django.shortcuts import render
from django.views.generic.edit import CreateView

from kontakt.forms import KontForm


class PostCreateView(CreateView):
    form_class = KontForm
    success_url = '/kontakt/kontakt'
    template_name = 'kontakt/kontakt.html'