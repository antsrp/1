from django.contrib import admin

from .models import Product, Purchase, Order

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Purchase)