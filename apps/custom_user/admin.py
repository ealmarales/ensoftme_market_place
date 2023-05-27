from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
import json
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import UserProfile
from .widgets import CustomGoogleMapsAddressWidget


# import custom forms

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

# Register your models here.
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','is_superuser', 'saldo']
    fieldsets = UserAdmin.fieldsets + (("Saldo", {'fields': ('saldo',)}),)
    

class UserProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': CustomGoogleMapsAddressWidget}
    }

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

