from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls')),
    url(r'', include('index.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^cennik/', include('cennik.urls')),
    url(r'^dane_kontaktowe/', include('dane_kontaktowe.urls')),
    url(r'^danedo_faktury/', include('danedo_faktury.urls')),
    url(r'^dodaj_ogloszenie/', include('dodaj_ogloszenie.urls')),
    url(r'^dodawanieogloszenia/', include('dodawanieogloszenia.urls')),
    url(r'^kategorie/', include('kategorie.urls')),
    url(r'^kontakt/', include('kontakt.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^logowanie/', include('logowanie.urls')),
    url(r'^mapakategorii/', include('mapakategorii.urls')),
    url(r'^mapamiejscowosci/', include('mapamiejscowosci.urls')),
    url(r'^mojekonto_ogloszenia/', include('mojekonto_ogloszenia.urls')),
    url(r'^mojekonto_ogloszeniav1/', include('mojekonto_ogloszeniav1.urls')),
    url(r'^oglosznie_widok/', include('oglosznie_widok.urls')),
    url(r'^pojedynczy_wpis/', include('pojedynczy_wpis.urls')),
    url(r'^pomoc/', include('pomoc.urls')),
    url(r'^regulamin/', include('regulamin.urls')),
    url(r'^rejestracja_dealer/', include('rejestracja_dealer.urls')),
    url(r'^rejestracja_indywidualny/', include('rejestracja_indywidualny.urls')),
    url(r'^rejestracja_indywidualna/', include('rejestracja_indywidualny.urls')),
    url(r'^ustawienia/', include('ustawienia.urls')),
    url(r'^wiadomosci/', include('wiadomosci.urls')),
    url(r'^wiadomosciv2/', include('wiadomosciv2.urls')),
    url(r'^zmien_haslo/', include('zmien_haslo.urls')),
]