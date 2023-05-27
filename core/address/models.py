from django.db import models
from django.utils.translation import gettext_lazy as _


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
    name_address = models.CharField(default= "", max_length=200, blank=False,)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    street = models.CharField(_('street'), max_length=255, blank=True, null=True)
    between_street1 = models.CharField(max_length=255, blank=True, null=True)
    nambetween_street1 = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(_('number'), max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name_address
