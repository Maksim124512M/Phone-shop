from django.contrib import admin

from phones.models import Phone, Order, Basket


admin.site.register(Phone)
admin.site.register(Order)
admin.site.register(Basket)
