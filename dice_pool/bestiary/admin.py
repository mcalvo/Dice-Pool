from monsters.models import Mon, Attack
from django.contrib import admin

#admin.site.register(Mon)

class AttacksInline(admin.TabularInline):
    model = Attack
    extra = 1

class MonAdmin(admin.ModelAdmin):
    inlines = [AttacksInline]
    list_display = ('name', 'level', 'role')
    list_filter = ['level']
    search_fields = ['name']

admin.site.register(Mon, MonAdmin)
