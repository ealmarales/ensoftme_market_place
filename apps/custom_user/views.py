from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView

from apps.custom_user import forms

from django.contrib.auth import get_user_model

from invitations.utils import get_invitation_model

from apps.custom_user.models import Beneficiary

User = get_user_model()

Invitation = get_invitation_model()


class ProfilePageView(LoginRequiredMixin,
                      UpdateView,
                      ):
    """View to edit personal data from the user profile"""
    form_class = forms.UserPersonalDataProfileForm
    contact_form_class = forms.UserContactDataProfileform

    template_name = "custom_user/profile/profile.html"
    success_url = reverse_lazy('custom_user:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'contact_form' not in context:
            context['contact_form'] = forms.UserContactDataProfileform(instance=self.request.user.profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object

        form = self.form_class(data=request.POST, instance=self.request.user)
        profile = request.user.profile
        contact_form = self.contact_form_class(data=request.POST, instance=profile)

        if form.is_valid() and contact_form.is_valid():
            form.save()
            contact_form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form,
                                                                 contact_form=contact_form,
                                                                 ))


class ProfileContactPageView(LoginRequiredMixin,
                             CreateView,
                             ):
    """
    View to add beneficiaries and update own information about a beneficiary in the user profile.
    """

    form_class = forms.BeneficiaryAddForm
    beneficiary_update_form_class = forms.BeneficiaryUpdateModelForm

    template_name = "custom_user/profile/profile_beneficiaries.html"
    success_url = reverse_lazy('custom_user:profile_contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'beneficiary_update_form_class' not in context:
            context['beneficiary_update_form'] = forms.BeneficiaryUpdateModelForm()
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['inviter'] = self.request.user
        return initial

    def post(self, request, *args, **kwargs):
        """
        Add a beneficiary or update the information saved about the beneficiary for logged user in user profile.

        If the submitted form contains an email field, then it is assumed that you want to add a new beneficiary;
        otherwise it is assumed that the information stored on a beneficiary is to be updated.

        Adding beneficiary:
            * When a user who is not in the system is added as a beneficiary, an invitation to register is sent to the
              beneficiary's email.

        """
        self.object = self.get_object

        if 'email' in request.POST:
            form = self.form_class(data=request.POST)
            if form.is_valid():
                beneficiary = form.save()
                try:
                    beneficiary.user = User.objects.get(email=form.cleaned_data.get('email'))
                    beneficiary.save()
                except User.DoesNotExist:
                    pass

                self.request.user.beneficiaries.add(beneficiary)

                # When a user who is not in the system is added as a beneficiary, an invitation to register is sent to
                # the beneficiary's email.
                if beneficiary.user is None:
                    invite = Invitation.create(form.cleaned_data.get('email'), inviter=request.user)
                    invite.send_invitation(request)

                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form))
        else:
            beneficiary_id = request.POST.get('beneficiary')
            beneficiary = get_object_or_404(Beneficiary, pk=beneficiary_id)
            update_form = self.beneficiary_update_form_class(data=request.POST, instance=beneficiary)
            if update_form.is_valid():
                update_form.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(beneficiary_update_form=update_form))


        return HttpResponseRedirect(self.success_url)


class ProfileAddressPageView(LoginRequiredMixin,
                             TemplateView
                             ):
    template_name = "custom_user/profile/profile_address.html"
