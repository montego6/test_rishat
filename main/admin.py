from django.contrib import admin
from .models import Item, StripeItem

admin.site.register(Item)
admin.site.register(StripeItem)
# Register your models here.
