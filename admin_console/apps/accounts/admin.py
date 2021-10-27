from django.contrib import admin
from .models import Customer, Gender


# Register your models here.
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    # exclude = ('name',)  # excludes fields
    fields = ('gender',)  # include fields
    # readonly_fields = ('gender',)  # read only fields
    # configurations for fields at display
    list_display = ('id', 'gender',)
    list_editable = ('gender',)


@admin.register(Customer)
class GenderAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    # exclude = ('name',)  # excludes fields
    fields = ('name', 'gender',)  # include fields
    # readonly_fields = ('name', 'gender',)  # read only fields
    # configurations for fields at display
    list_display = ('id', 'name', 'gender',)
    list_editable = ('name', 'gender',)