from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'markdown_proj.views.home', name='home'),
    # url(r'^markdown_proj/', include('markdown_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
