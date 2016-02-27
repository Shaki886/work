from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mojekonto_ogloszeniav1, name='mojekonto_ogloszeniav1'),
]