from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bestiary.views',
    url(r'^$', 'index', name = 'monList'),
    url(r'^(?P<mon_id>\d+)/$', 'detail', name = 'detail'),
    url(r'^create/$', 'create'),
    url(r'^(?P<mon_id>\d+)/power/$', 'power'),
)
