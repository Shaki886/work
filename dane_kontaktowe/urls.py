from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dane_kontaktowe, name='dane_kontaktowe'),
]