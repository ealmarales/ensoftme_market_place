from django.db import models
from django.utils.translation import gettext_lazy as _
from django_google_maps import fields as map_fields


# Create your models here.
class Country(models.Model):
    name = models.CharField(_('country'), max_length=255, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class Province(models.Model):
    name = models.CharField(_('province'), max_length=255, )
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} / {self.country}"


class Municipality(models.Model):
    name = models.CharField(_('nunicipality'), max_length=255, )
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} / {self.province}"


class Address(models.Model):
    name_address = models.CharField(max_length=200)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.name_address
