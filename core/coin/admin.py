from django.contrib import admin

# Register your models here.
from core.coin.models import Coin


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('iso_code', 'name', 'symbol', )