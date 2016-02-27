from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rejestracja_indywidualny, name='rejestracja_indywidualny'),
]