from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.custom_user.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ When a user registers, their corresponding profile is created.

    """
    if created:
        instance.profile = Profile()
        instance.profile.save()
