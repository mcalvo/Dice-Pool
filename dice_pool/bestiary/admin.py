from django.contrib import admin
from bestiary.models import Monster

#admin.site.register(Mon)
"""
class AttacksInline(admin.TabularInline):
    model = Attack
    extra = 1
"""

class MonsterAdmin(admin.ModelAdmin):
    #inlines = [AttacksInline]
    list_display = ('name', 'level', 'role')
    list_filter = ['level']
    search_fields = ['name']

admin.site.register(Monster, MonsterAdmin)
