from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django_google_maps import fields as map_fields
# Create your models here.



class CustomUser(AbstractUser):
    saldo = models.FloatField(default=0)
    


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    