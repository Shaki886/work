from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('index.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^kontakt/', include('kontakt.urls')),
]