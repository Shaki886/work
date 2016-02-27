from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wiadomosciv2, name='wiadomosciv2'),
]