from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
from django.utils.translation import gettext_lazy as _

from django.db import models

User = get_user_model()


class Beneficiary(models.Model):
    beneficiary = models.ForeignKey(User, on_delete=models.CASCADE)
    decription = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.decription:
            return self.decription
        return self.beneficiary


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    saldo = models.FloatField(default=0)

    phone_number = models.CharField(_('phone number'), max_length=10, null=True, blank=True)
    address = map_fields.AddressField(_('address'), max_length=200, null=True, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)

    beneficiaries = models.ManyToManyField(Beneficiary, related_name='beneficiaries')

    def __str__(self):
        return self.user.__str__()
