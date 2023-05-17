from django.contrib import admin

# Register your models here.
from core.address.models import Country, Province, Municipality


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
