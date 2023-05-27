from django.urls import path

from . import views

app_name = 'address'

urlpatterns = [
    path('provinces/', views.fetch_provinces, name='fetch_provinces'),
    path('municipalities/', views.fetch_municipalities, name='fetch_municipalities'),
]
