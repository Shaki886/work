from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rejestracja_dealer, name='rejestracja_dealer'),
]