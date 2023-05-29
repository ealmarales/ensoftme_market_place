from django.contrib import admin
from django_google_maps import fields as map_fields
from .models import Profile
from .widgets import CustomGoogleMapsAddressWidget


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': CustomGoogleMapsAddressWidget}
    }


admin.site.register(Profile, UserProfileAdmin)

