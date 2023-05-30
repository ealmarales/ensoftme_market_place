from django.urls import path

from apps.custom_user import views

app_name = 'custom_user'

urlpatterns = [
    path("profile", views.ProfilePageView.as_view(), name="profile"),
]
