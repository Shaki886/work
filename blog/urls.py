from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/?$', 'blog.views.post_list', name='post-list'),
	url(r'^(?P<page>[0-9]+)/$', 'blog.views.post_list', name='post-list'),
	url(r'^/?$', 'blog.views.view_list', name='view-list'),
	]