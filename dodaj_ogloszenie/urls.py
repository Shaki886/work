from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dodaj_ogloszenie, name='dodaj_ogloszenie'),
]