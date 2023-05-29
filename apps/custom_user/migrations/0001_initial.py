# Generated by Django 4.2.1 on 2023-05-29 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.FloatField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', django_google_maps.fields.AddressField(blank=True, max_length=200, null=True)),
                ('geolocation', django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
