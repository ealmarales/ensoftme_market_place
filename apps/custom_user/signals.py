from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from apps.custom_user.models import Profile


@receiver(user_signed_up)
def populate_profile(sociallogin, user, **kwargs):
    """ When a user registers, their corresponding profile is created. """
    if sociallogin.account.provider == 'google':
        # user_data = user.socialaccount_set.filter(provider='google')[0].extra_data
        user.profile = Profile()
    user.profile.save()
