from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ogloszenie_widok, name='ogloszenie_widok'),
]