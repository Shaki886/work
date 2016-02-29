from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.UserCreateView.as_view(), name='create_user'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'form.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
)