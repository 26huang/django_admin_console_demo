from django.contrib import admin
from .models import Customer, Gender, ZipCode, Status


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
class CustomerAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    # exclude = ('name',)  # excludes fields
    fields = ('name', 'gender', )  # include fields
    # readonly_fields = ('name', 'gender',)  # read only fields
    # configurations for fields at display
    list_display = ('id', 'name', 'gender',)
    list_editable = ('name', 'gender',)


@admin.register(ZipCode)
class ZipCodeAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    # exclude = ('name',)  # excludes fields
    fields = ('zip_code',)  # include fields
    # readonly_fields = ('name', 'gender',)  # read only fields
    # configurations for fields at display
    list_display = ('id', 'zip_code',)
    list_editable = ('zip_code',)


@admin.register(Status)
class ZipCodeAdmin(admin.ModelAdmin):
    # configuration for fields when adding new records
    # exclude = ('name',)  # excludes fields
    fields = ('customer', 'zip_code', 'active')  # include fields
    # readonly_fields = ('name', 'gender',)  # read only fields
    # configurations for fields at display
    list_display = ('id', 'customer', 'zip_code', 'active',)
    list_editable = ('customer', 'zip_code', 'active',)