from django.contrib import admin
from .models import Category, Pet, CartItem, Order


admin.site.register(Category)
admin.site.register(Pet)
admin.site.register(CartItem)
admin.site.register(Order)

