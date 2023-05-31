# from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ProfilePageView(TemplateView):
    template_name = "market/profile/profile.html"


class ProfileContactPageView(TemplateView):
    template_name = "market/profile/profile_contacts.html"


class ProfileAddressPageView(TemplateView):
    template_name = "market/profile/profile_address.html"
