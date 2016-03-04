from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^/?$', 'kontakt.views.kontakt', name='kontakt'),
	url(r'^ok/?$', 'kontakt.views.ok', name='kontaktok'),
]