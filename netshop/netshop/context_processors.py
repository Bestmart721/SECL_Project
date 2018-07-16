# -*- coding: utf-8 -*-
from __future__ import absolute_import
from person.views import Person


def get_data():
    return Person.objects.get(pk=1)

def netshop(request):
    """Short context manager
    added into footer my name from db"""
    context = {'author': get_data}
    return context