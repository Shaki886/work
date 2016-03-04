from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.kontakt, name='kontakt'),
    url(r'^ok/$', views.ok, name='kontaktok'),
]