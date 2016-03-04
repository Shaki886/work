from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^post/(?P<page>[0-9]+)/$', views.ViewList.as_view(), name='view-list'),
	]