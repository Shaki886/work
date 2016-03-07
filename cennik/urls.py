from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/?$', 'cennik.views.cennik', name='cennik'),
]