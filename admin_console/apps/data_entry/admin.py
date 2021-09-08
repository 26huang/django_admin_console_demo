from django.contrib import admin
from .models import Object, Position
from django.contrib.auth.models import Group

admin.site.site_header = 'WARCHEST'

# admin.site.register(Object)
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    # exclude = ('name',)  # excludes fields
    fields = ('name', 'hash_val')  # include fields
    readonly_fields = ('name', 'hash_val')  # read only fields
    # configurations for fields at display
    list_display = ('id', 'name', 'hash_val')
    list_editable = ('name', 'hash_val')


# admin.site.register(Position)
@admin.register(Position)
class MoveAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    fields = ('object', 'message',)
    readonly_fields = ('message',)

    # configurations for fields at display
    list_display = ('id', 'object', 'latitude', 'longitude', 'last_active', 'start_time', 'status', 'message',)
    list_editable = ('status',)
    list_filter = ('object', 'id',)


# admin.site.unregister(Group)