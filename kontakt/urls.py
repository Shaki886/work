from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'^/?$', 'kontakt.views.kontakt', name='kontakt'),
]