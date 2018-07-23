# -*- coding: utf-8 -*-
from django.shortcuts import render
from person.models import Person
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, UpdateView, CreateView


def person(request):
    """The list of persons"""
    person_list = Person.objects.all()
    context = {
        'person': person_list
    }
    return render(request, 'person/person.html', context)

@require_http_methods(['POST', 'GET'])
def person_detail(request, pk):
    """The details of person method"""
    person = get_object_or_404(Person, pk=pk)
    context = {'person': person}
    return render(request, 'person/person_detail.html', context)

class CustomPersonDetailView(TemplateView):
    template_name = 'person/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomPersonDetailView, self).get_context_data(**kwargs)
        context['person'] = get_object_or_404(Person, pk=kwargs['pk'])
        return context

class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'