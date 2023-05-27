from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.custom_user.models import CustomUser
from core.address.models import Province
from core.coin.models import Coin

CURRENCY_PROVIDER_STATUS_CHOICE = (
    ('CREATED', _('CREATED')),
    ('IN_VALIDATION', _('IN_VALIDATION')),
    ('VALIDATED', _('VALIDATED')),
    ('BANNED', _('BANNED'))
)


class CoinProvider(CustomUser):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    # tasa de cambio USD - MLC precio disponiblilidad
    status = models.CharField(max_length=20, choices=CURRENCY_PROVIDER_STATUS_CHOICE, default='CREATED')


class CoinExchangeOffer(models.Model):
    coin_origin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_origin')
    coin_provider = models.ForeignKey(CoinProvider, on_delete=models.CASCADE)
    coin_exchange = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_exchange')
    exchange_tax = models.DecimalField(_("seller's profit per unit sold"), validators=[MinValueValidator(0)],
                                    decimal_places=2, max_digits=6)
    available_amount = models.DecimalField(_("available amount"), validators=[MinValueValidator(1)], decimal_places=2,
                                        max_digits=6)

    class Meta:
        verbose_name = _('Coin Exchange Offer')
        unique_together = ('coin_provider', 'coin_origin', 'coin_exchange')


class Operation(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipient')
    tax = models.DecimalField(_("available amount"), validators=[MinValueValidator(0)], decimal_places=2, max_digits=6)


class MarketConfig(models.Model):
    fee = models.DecimalField(_("fee in %"), validators=[MinValueValidator(0)], decimal_places=2, max_digits=6)
