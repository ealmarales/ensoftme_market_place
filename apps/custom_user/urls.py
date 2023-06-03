from django.urls import path

from apps.custom_user import views

app_name = 'custom_user'

urlpatterns = [
    path("profile", views.ProfilePageView.as_view(), name="profile"),
    path("profile/contacts", views.ProfileContactPageView.as_view(), name="profile_contacts"),
    path("profile/address", views.ProfileAddressPageView.as_view(), name="profile_address"),
]
