from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


class Command(BaseCommand):
    help = 'Adds social apps to the database'

    def handle(self, *args, **options):        
        current_site = Site.objects.get_or_create(domain='127.0.0.1:8000', name='127.0.0.1:8000')[0]
        #current_site = get_current_site(None)

        social_apps = [
            {
                'provider': 'google',
                'name': 'Google',
                'client_id': settings.GOOGLE_CLIENT_ID,
                'secret': settings.GOOGLE_CLIENT_SECRET,
                'sites': [current_site.id],
            },
            # Agrega aquí las otras aplicaciones sociales que desees configurar
        ]

        for app in social_apps:
            try:
                social_app = SocialApp.objects.get(provider=app['provider'])
                self.stdout.write(self.style.WARNING(f'Social app {app["name"]} already exists. Skipping...'))
            except SocialApp.DoesNotExist:
                social_app = SocialApp(
                    provider=app['provider'],
                    name=app['name'],
                    client_id=app['client_id'],
                    secret=app['secret'],
                )
                social_app.save()
                social_app.sites.set(app['sites'])
                self.stdout.write(self.style.SUCCESS(f'Social app {app["name"]} created successfully!'))
