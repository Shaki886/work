from django.shortcuts import render
from django.views.generic.edit import CreateView

from kontakt.forms import KontForm
from kontakt.models import Kontakt


class PostCreateView(CreateView):
    model = Kontakt
    form_class = KontForm
    success_url = '/kontakt/kontakt'
    template_name = 'kontakt/kontakt.html'