from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.kategorie, name='kategorie'),
]