from django.contrib import admin
from .models import Item, StripeItem, Order

admin.site.register(Item)
admin.site.register(StripeItem)
admin.site.register(Order)
# Register your models here.
