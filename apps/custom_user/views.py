from django. contrib. auth. mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, FormView

from apps.custom_user import forms
from apps.custom_user import models


class ProfilePageView(LoginRequiredMixin,
                      UpdateView,
                      ):
    """View to edit personal data from the user profile"""
    form_class = forms.UserPersonalDataProfileForm
    contact_form_class = forms.UserContactDataProfileform

    template_name = "custom_user/profile/profile.html"
    success_url = reverse_lazy('custom_user:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'contact_form' not in context:
            context['contact_form'] = forms.UserContactDataProfileform(instance=self.request.user.profile)
        return context

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        profile = request.user.profile
        contact_form = self.contact_form_class(data=request.POST, instance=profile)

        if form.is_valid() and contact_form.is_valid():
            form.save()
            contact_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class ProfileContactPageView(LoginRequiredMixin,
                             FormView,
                             ):
    """View to edit contact data from the user profile"""
    form_class = forms.BeneficiaryAddForm
    template_name = "custom_user/profile/profile_contacts.html"


class ProfileAddressPageView(LoginRequiredMixin,
                             TemplateView
                             ):
    template_name = "custom_user/profile/profile_address.html"
