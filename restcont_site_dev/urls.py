from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(

    '',
    url( r'^$', 'WebDevelopment.views.home', name='home' ),
    url( r'^home/', 'WebDevelopment.views.home', name='home' ),
    url( r'^development/', 'WebDevelopment.views.development', name='development' ),
    url( r'^design/', 'WebDevelopment.views.design', name='design' ),
    url( r'^marketing/', 'WebDevelopment.views.marketing', name='marketing' ),
    url( r'^portfolio/', 'WebDevelopment.views.portfolio', name='portfolio' ),
    url( r'^products/', 'WebDevelopment.views.products', name='products' ),
    url( r'^contact/', 'WebDevelopment.views.contact', name='contact' ),
    url( r'^about/', 'WebDevelopment.views.about', name='about' ),
    url( r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG :
	urlpatterns == static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )
	urlpatterns == static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )