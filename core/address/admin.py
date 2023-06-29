from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
from core.address.models import Country, Province, Municipality, Address


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )
    list_filter = ('country', )


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', )
    list_filter = ('province', )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }