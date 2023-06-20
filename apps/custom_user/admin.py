from django.contrib import admin
from django_google_maps import fields as map_fields

from . import models

from .widgets import CustomGoogleMapsAddressWidget


# Register your models here.
@admin.register(models.Profile)
class UserProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': CustomGoogleMapsAddressWidget}
    }


@admin.register(models.Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('pk','email', 'user', 'inviter','decription', )
    list_filter = ('inviter', )
