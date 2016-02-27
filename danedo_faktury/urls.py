from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.danedo_faktury, name='danedo_faktury'),
]