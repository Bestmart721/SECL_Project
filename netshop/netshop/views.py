# -*- coding: utf-8 -*-
from django.shortcuts import render

def main(request):
    """This view is connected to the main folder
    templates and file home.html"""
    return render(request, 'home.html')


