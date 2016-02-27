from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pojedynczy_wpis, name='pojedynczy_wpis'),
]