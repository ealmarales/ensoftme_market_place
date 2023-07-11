from django.db import models
from django.utils.translation import gettext_lazy as _
from django_google_maps import fields as map_fields


# Create your models here.
class Country(models.Model):
    name = models.CharField(_('country'), max_length=255, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('pais')
        verbose_name_plural = _('paises')


class Province(models.Model):
    name = models.CharField(_('provincia'), max_length=255, )
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('provincia')
        verbose_name_plural = _('provincias')


class Municipality(models.Model):
    name = models.CharField(_('nunicipality'), max_length=255, )
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('municipio')
        verbose_name_plural = _('municipios')


class Address(models.Model):
    name_address = models.CharField(_('descripción'), max_length=200)
    address = map_fields.AddressField(max_length=200, verbose_name=_('dirección'))

    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('pais'))
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('provincia'))
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_('municipio'))

    geolocation = map_fields.GeoLocationField(max_length=100, verbose_name=_('coordenadas'))

    def __str__(self):
        return self.name_address

    class Meta:
        verbose_name = _('dirección')
        verbose_name_plural = _('direcciones')
