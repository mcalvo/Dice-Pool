from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('base.views',
	url(r'^$',			'root',						name='site_index'),
) + patterns('',
    url(r'^admin/', 	include(admin.site.urls)),
    url(r'^bestiary/', 	include('bestiary.urls')),
) + staticfiles_urlpatterns()
