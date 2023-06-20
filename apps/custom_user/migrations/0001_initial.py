# Generated by Django 4.2.1 on 2023-06-19 14:08

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
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='phone number')),
                ('address', django_google_maps.fields.AddressField(blank=True, max_length=200, null=True, verbose_name='address')),
                ('geolocation', django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decription', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beneficiaries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'beneficiary',
                'verbose_name_plural': 'beneficiaries',
                'unique_together': {('email', 'inviter')},
            },
        ),
    ]
