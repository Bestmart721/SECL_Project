# -*- coding: utf-8 -*-
import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from shop.models import Shop, TypeShop
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from  shop.forms import ShopForm

def shop(request):
    shop_list = Shop.objects.all()
    context = {
        'shop': shop_list
    }
    return render(request, 'shop/shop.html', context)

# @require_http_methods(['POST', 'GET'])
# def shop_detail(request, pk):
#     shop = get_object_or_404(Shop, pk=pk)
#     context = {'shop': shop}
#     return render(request, 'shop/shop_detail.html', context)

class CustomShopDetailView(TemplateView):
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomShopDetailView, self).get_context_data(**kwargs)
        context['object'] = get_object_or_404(Shop, pk=kwargs['pk'])
        return context

# class ShopUpdateView(UpdateView):
#     template_name = 'shop/shop_form.html'
#     model = Shop
#     fields = ('name', 'seller', 'type_of_shop')
#
# class ShopCreateView(CreateView):
#     template_name = 'shop/shop_form.html'
#     model = Shop
#     fields = ('type_of_shop', 'name', 'owner', 'seller', 'stock', 'city', 'website')



def shop_edit(request, pk):
    if pk == 'new':
        instance = None
    else:
        instance = get_object_or_404(Shop, pk=pk)
    form = ShopForm(request.POST or None, instance=instance)
    if form.is_valid():
        shop = form.save()
        messages.success(request, 'OK')
        return redirect('shop_edit', pk=shop.pk)
    return render(request, 'shop/shop_edit.html', {'form': form})

def type(request):
    typeof = TypeShop.objects.all()
    context = {
        'type': typeof
    }
    return render(request, 'shop/type.html', context)

def type_detail(request, pk):
    typeof = get_object_or_404(TypeShop, pk=pk)
    context = {
        'type' : typeof
    }
    return  render(request, 'shop/type_detail.html', context)

class TypeUpdateView(UpdateView):
    model = TypeShop
    fields = ('name',)

class TypeCreateView(CreateView):
    model = TypeShop
    fields = ('name',)



def test(request):
    shop = Shop.objects.all()
    mes = messages.success(request, 'Okey')
    context = {
        'shop': shop,
        'test': timezone.now(),
        'date_prefix': 'date: ',
        't': 'Vova',
        'message': mes,
        'selected_menu': random.randint(0,2)
    }
    return render(request, 'shop/test.html', context)

