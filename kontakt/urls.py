from django.conf.urls import patterns, url

from kontakt import views

urlpatterns = patterns(
    '',
    url(r'^add/$', views.PostCreateView.as_view(), name='kontakt'),
)