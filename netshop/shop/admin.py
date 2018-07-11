from django.contrib import admin
from shop.models import TypeShop, Shop

# Register your models here.
admin.site.register(Shop)
admin.site.register((TypeShop))