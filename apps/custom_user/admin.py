from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Profile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'user', 'inviter', 'decription', )
    list_filter = ('inviter', )
