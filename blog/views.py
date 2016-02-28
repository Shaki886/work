from django.shortcuts import render
from .models import Postform

def Blog(request):

    blog = Blog.objects.order_by()

    return render(request, 'blog/blog.html', {'blogs': blogs})

def Kategorie_aut(request):

    kategorie = Kategorie_aut.objects.order_by()

    return render(request, 'blog/blog.html', {'kategorie': kategorie})