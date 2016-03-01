from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/?$', 'pojedynczy_wpis.views.post', name='post'),
	url(r'^(?P<page>[0-9]+)/$', 'pojedynczy_wpis.views.post', name='post'),
	]