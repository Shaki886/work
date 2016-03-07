from django.shortcuts import render
from .models import Indywidualny

def indywidualny_list (request):
	queryset = Post.objects.all()
	context = {
		"indywidualny_list": queryset,
		}
    return render(request, "cennik.html", context)