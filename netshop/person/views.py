# -*- coding: utf-8 -*-
from django.shortcuts import render
from person.models import Person
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


def person(request):
    """The list of persons"""
    person_list = Person.objects.all()
    context = {
        'person': person_list
    }
    return render(request, 'person/person.html', context)

@require_http_methods(['POST', 'GET'])
def person_detail(request, person_id):
    """The details of person method"""
    person = get_object_or_404(Person, pk=person_id)
    context = {'person': person}
    return render(request, 'person/person_detail.html', context)
