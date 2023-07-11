from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django_google_maps.fields import AddressField, GeoLocationField

from apps.custom_user import models
from core.address.models import Address, Country, Province, Municipality


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


class UserProfileContactDataForm(forms.ModelForm):
    """
    Used to edit contact data from users.
    """
    class Meta:
        model = models.Profile
        fields = ['phone_number', ]


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


class KnowAddressAddForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class KnowAddressUpdateFormClass(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class ProfileForm(forms.Form):
    action = forms.CharField(max_length=100)

    # personal data user profile
    first_name = forms.CharField(label=_('first name'), max_length=255)
    last_name = forms.CharField(label=_('last name'), max_length=255)
    email = forms.EmailField(label=_('email'), )

    # contact data user profile
    phone_number = forms.CharField(label=_('número telefónico'), max_length=50)

    # address
    name_address = forms.CharField(label=_('descripción'), max_length=200)
    country = forms.ModelChoiceField(label=_('país'), queryset=Country.objects.all())
    province = forms.ModelChoiceField(label=_('provincia'), queryset=Province.objects.all())
    municipality = forms.ModelChoiceField(label=_('municipio'), queryset=Municipality.objects.all())
    # address = AddressField(max_length=200)
    # geolocation = GeoLocationField(max_length=100)
    # TODO: utilizar los campos para renderizar el mapa de googlemap

    # beneficiary
    beneficiary_email = forms.EmailField(label=_('email'), )
    beneficiary_phone_number = forms.CharField(label=_('número telefónico'), max_length=50)
    beneficiary_decription = forms.CharField(label=_('descripción'), max_length=255)
    beneficiary_inviter = forms.HiddenInput()




