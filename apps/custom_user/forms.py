from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

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


class BeneficiaryAddForm(forms.ModelForm):
    """
    Used to add beneficiaries to user profile.
    """
    class Meta:
        model = models.Beneficiary
        fields = ['email',
                  'phone_number',
                  'decription',
                  'inviter',
                  ]
        widgets = {
            'inviter': forms.HiddenInput()
        }


class BeneficiaryUpdateModelForm(forms.ModelForm):
    """ Used to update beneficiaries data. """
    beneficiary = forms.IntegerField()  # beneficiary identifier to update

    class Meta:
        model = models.Beneficiary
        fields = ['phone_number',
                  'decription',
                  'beneficiary',
                  ]

        widgets = {
            'beneficiary': forms.HiddenInput()
        }
        # TODO: hide beneficiary field
