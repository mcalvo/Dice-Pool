from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bestiary.views',
    url(r'^$', 				'index', 	name = "bestiary_mon_listing"),
    url(r'^(?P<mon_id>\d+)/$', 		'detail', 	name = "bestiary_mon_detail"),
    url(r'^create/$', 			'create', 	name = "bestiary_create_mon"),
    url(r'^(?P<mon_id>\d+)/power/$', 	'power', 	name = "bestiary_create_power"),
)
