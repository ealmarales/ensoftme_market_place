from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django.utils.translation import gettext_lazy as _

from apps.custom_user import models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class UserPersonalDataProfileForm(forms.ModelForm):
    """
    Used to edit personal data from users.
    """
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']


class UserContactDataProfileform(forms.ModelForm):
    """
    Used to edit contact data from users.
    """
    class Meta:
        model = models.Profile
        fields = ['phone_number', 'address', ]


class BeneficiaryAddForm(forms.Form):
    """
    Used to add beneficiaries to user profile.
    """
    email = forms.EmailField(label=_('email'), )
    phone_number = forms.CharField(label=_('phone number'), max_length=10, required=False)
    decription = forms.CharField(label=_('description'), max_length=255, required=False)
