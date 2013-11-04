from django.contrib import admin
from bestiary import models as bestiarymodels

#admin.site.register(Mon)

class MonsterAdmin(admin.ModelAdmin):
   list_display = ('name', 'level', 'role')
   list_filter = ['level']
   search_fields = ['name']

admin.site.register(bestiarymodels.Usage)
admin.site.register(bestiarymodels.MonsterRole)
admin.site.register(bestiarymodels.Ability)
admin.site.register(bestiarymodels.Attack)
admin.site.register(bestiarymodels.Monster, MonsterAdmin)
