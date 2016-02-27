from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.zmien_haslo, name='zmien_haslo'),
]