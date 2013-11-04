from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bestiary.forms import AbilityForm, AttackForm

admin.autodiscover()

urlpatterns = patterns('bestiary.views',
   url(r'^$', 							                        'monsterListing',               		   name = "bestiary_monsterListing"),
   url(r'^(?P<mon_id>\d+)/$', 			                  'monsterDetail', 		                  name = "bestiary_monsterDetail"),
   url(r'^create/$', 					                     'editMonster',	 	                     name = "bestiary_createMonster"),
   url(r'^(?P<mon_id>\d+)/ability/$',                    'editAbility', {'form': AbilityForm },	name = "bestiary_createAbility"),
   url(r'^(?P<mon_id>\d+)/attack/$', 	                  'editAbility', {'form': AttackForm },	name = "bestiary_createAttack"),
   url(r'^(?P<mon_id>\d+)/ability/(?P<ability_id>\d+)/$','editAbility', {'form': AbilityForm },	name = "bestiary_editAbility"),
   url(r'^(?P<mon_id>\d+)/attack/(?P<attack_id>\d+)/$', 	'editAbility', {'form': AttackForm },	name = "bestiary_editAttack"),
)
