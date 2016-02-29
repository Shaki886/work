from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<page>[0-9]+)/$', 'blog.views.blog', name='post-list'),
	url(r'^/?$', 'blog.views.blog', name='post-list'),
]