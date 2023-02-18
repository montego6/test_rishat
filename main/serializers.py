from rest_framework import serializers
from .models import Order, Item, Tax


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.CharField(source='stripe.price')
    quantity = serializers.IntegerField(default=1, initial=1)
    tax_rates = serializers.SerializerMethodField('get_tax_rate')

    class Meta:
        model = Item
        fields = ('price', 'quantity', 'tax_rates')

    def get_tax_rate(self, obj):
        tax = Tax.objects.get(id=1)
        return [tax.stripe]


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('items',)