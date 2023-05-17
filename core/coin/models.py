from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Coin(models.Model):
    iso_code = models.CharField(_('iso code'), max_length=3, primary_key=True)
    name = models.CharField(_('name'), max_length=50)
    symbol = models.CharField(_('symbol'), max_length=3)
