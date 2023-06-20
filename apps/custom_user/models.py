from django.contrib.auth import get_user_model
from invitations.utils import get_invitation_model

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django_google_maps import fields as map_fields
from django.utils.translation import gettext_lazy as _

from django.db import models

User = get_user_model()


class Beneficiary(models.Model):
    """
    Represent a beneficiary. A beneficiary is a person to whom money is frequently sent.

    Notes:
        * when a beneficiary is not registered in the system, his associated user is null.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='beneficiaries')
    decription = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=10, null=True, blank=True)

    email = models.EmailField()  # user email identifier
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited')  # invitation sender

    def __str__(self):
        if self.decription:
            return self.decription
        return self.email

    class Meta:
        verbose_name = _("beneficiary")
        verbose_name_plural = _("beneficiaries")
        unique_together = ('email', 'inviter')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    saldo = models.FloatField(default=0)

    phone_number = models.CharField(_('phone number'), max_length=10, null=True, blank=True)
    address = map_fields.AddressField(_('address'), max_length=200, null=True, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.__str__()
