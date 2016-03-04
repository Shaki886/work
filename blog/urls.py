from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/?$', views.PostList.as_view(), name='post-list'),
	url(r'^(?P<page>[0-9]+)/$', views.PostList.as_view(), name='post-list'),
	url(r'^post/(?P<page>[0-9]+)/$', views.ViewList.as_view(), name='view-list'),
	]