# -*- coding: utf-8 -*-
from django.shortcuts import render
from place.models import Country, City
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


def place(request):
    city_list = City.objects.all()
    context = {
        'city': city_list
    }
    return render(request, 'place/place.html', context)

@require_http_methods(['POST', 'GET'])
def place_detail(request, place_id):
    place = get_object_or_404(City, pk=place_id)
    context = {'place': place}
    return render(request, 'place/place_detail.html', context)
