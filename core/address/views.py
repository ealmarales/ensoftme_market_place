from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Country, Province, Municipality


def fetch_provinces(request):
    country_id = request.GET.get('country_id')
    country = get_object_or_404(Country, id=country_id)
    provinces = country.province_set.all()
    data = {'provinces': [{'id': p.id, 'name': p.name} for p in provinces]}
    return JsonResponse(data)


def fetch_municipalities(request):
    province_id = request.GET.get('province_id')
    province = get_object_or_404(Province, id=province_id)
    municipalities = province.municipality_set.all()
    data = {'municipalities': [{'id': m.id, 'name': m.name} for m in municipalities]}
    return JsonResponse(data)
