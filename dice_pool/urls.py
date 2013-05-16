from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('dice_pool.core.views',
    url(r'^$', 		'root', 	name='root'),	
) + patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bestiary/', include('dice_pool.bestiary.urls')),
)
