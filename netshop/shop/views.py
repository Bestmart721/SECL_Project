# -*- coding: utf-8 -*-
from django.shortcuts import render
from shop.models import Shop, TypeShop
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy




def shop(request):
    shop_list = Shop.objects.all()
    context = {
        'shop': shop_list
    }
    return render(request, 'shop/shop.html', context)

@require_http_methods(['POST', 'GET'])
def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    context = {'shop': shop}
    return render(request, 'shop/shop_detail.html', context)

class ShopUpdateView(UpdateView):
    model = Shop
    fields = ('type_of_shop', 'name', 'owner', 'seller', 'stock', 'city', 'website')

class ShopCreateView(CreateView):
    model = Shop
    fields = ('type_of_shop', 'name', 'owner', 'seller', 'stock', 'city', 'website')

def type(request):
    typeof = TypeShop.objects.all()
    context = {
        'type': typeof
    }
    return render(request, 'shop/type.html', context)

def type_detail(request, type_id):
    typeof = get_object_or_404(TypeShop, pk=type_id)
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

class CustomShopCreateView(TemplateView):
    template_name = 'shop/shop_form.html'

    def get_context_data(self, **kwargs):
        fields = ('type_of_shop', 'name', 'owner', 'seller', 'stock', 'city', 'website')
        context = super(CustomShopCreateView, self).get_context_data(**kwargs)
        context['object'] = get_object_or_404(Shop, pk=1)
        return context

