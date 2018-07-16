# -*- coding: utf-8 -*-
from django.shortcuts import render
from stock.models import Stock
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import DeleteView, UpdateView, CreateView



def stock(request):
    stock_list = Stock.objects.all()
    context = {
        'stock': stock_list
    }
    return render(request, 'stock/stock.html', context)

@require_http_methods(['POST', 'GET'])
def stock_detail(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    context = {'stock': stock}
    return render(request, 'stock/stock_detail.html', context)

class StockUpdateView(UpdateView):
    model = Stock
    fields = ('name', 'city', 'adress')

class StockCreateView(CreateView):
    model = Stock
    fields = ('name', 'city', 'adress')

