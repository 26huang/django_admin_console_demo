from django.contrib import admin
from .models import Object, Position

admin.site.site_header = 'WARCHEST'

# admin.site.register(Object)
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)


# admin.site.register(Position)
@admin.register(Position)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'latitude', 'longitude', 'last_active', 'start_time', 'status',)
    list_editable = ('status',)
    list_filter = ('object',)