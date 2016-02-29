from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.UserCreateView.as_view(), name='create_user'),
)