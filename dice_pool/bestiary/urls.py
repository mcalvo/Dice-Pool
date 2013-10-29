from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bestiary.views',
    url(r'^$', 							'mon_listing', 		name = "bestiary_mon_listing"),
    url(r'^(?P<mon_id>\d+)/$', 			'mon_detail', 		name = "bestiary_mon_detail"),
    url(r'^create/$', 					'create_mon',	 	name = "bestiary_create_mon"),
    #url(r'^(?P<mon_id>\d+)/power/$', 	'create_power', 	name = "bestiary_create_power"),
)
