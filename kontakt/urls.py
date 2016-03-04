from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.kontakt, name='kontakt'),
    url(r'^ok/$', {'template_name': 'ok.html'}, name='kontaktok'),
]