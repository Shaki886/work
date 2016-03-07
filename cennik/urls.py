from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/?$', 'cennik.views.indywidualny_list', name='cennik'),
]