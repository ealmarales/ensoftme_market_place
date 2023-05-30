from django.urls import path, include

from .views import HomePageView

app_name = 'market'

urlpatterns = [
    path("", HomePageView. as_view(), name="home"),
]
