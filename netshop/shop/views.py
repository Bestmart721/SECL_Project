# -*- coding: utf-8 -*-
from django.shortcuts import render
from shop.models import Shop, TypeShop
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


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
