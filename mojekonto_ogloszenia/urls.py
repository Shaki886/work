from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mojekonto_ogloszenia, name='mojekonto_ogloszenia'),
]