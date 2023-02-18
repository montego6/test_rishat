from rest_framework import serializers
from .models import Order, Item


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.CharField(source='stripe.price')
    quantity = serializers.IntegerField(default=1, initial=1)

    class Meta:
        model = Item
        fields = ('price', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('items',)