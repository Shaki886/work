from django.conf.urls import patterns, url

from kontakt import views

urlpatterns = patterns(
    '',
    url(r'^$', views.PostCreateView.as_view(), name='kontakt'),
)