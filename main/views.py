from django.shortcuts import render
from .models import Item

# Create your views here.


def item_retrieve(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item.html', {'item': item})