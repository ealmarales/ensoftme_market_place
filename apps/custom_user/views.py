from django. contrib. auth. mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "market/profile/profile.html"


class ProfileContactPageView(LoginRequiredMixin, TemplateView):
    template_name = "market/profile/profile_contacts.html"


class ProfileAddressPageView(LoginRequiredMixin, TemplateView):
    template_name = "market/profile/profile_address.html"
