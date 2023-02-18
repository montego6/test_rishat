from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .models import Item, Order
from .serializers import OrderSerializer
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
import json


stripe.api_key = config('STRIPE_KEY')
# Create your views here.


def item_retrieve(request, id):
    item = Item.objects.get(id=id)
    cart = request.session.get('cart', [])
    cart_items = Item.objects.filter(id__in=cart)
    return render(request, 'item.html', {'item': item, 'cart_items': cart_items})


def buy_success(request):
    return render(request, 'success.html')


class BuyItemAPIView(APIView):
    def get(self, request, id):
        item = Item.objects.get(id=id)
        session = stripe.checkout.Session.create(
            success_url=request.build_absolute_uri(reverse('buy-success')),
            line_items=[
                {
                    "price": item.stripe.price,
                    "quantity": 1,
                },
            ],
            mode="payment",
        )
        return Response({'id': session['id']})


def add_to_order(request, id):
    cart = request.session.get('cart', [])
    if id not in cart:
        cart.append(id)
    request.session['cart'] = cart
    print(cart)
    return JsonResponse({'status': f'{id} added to cart'})


def clear_order(request):
    request.session['cart'] = []
    return JsonResponse({'status': 'cart is cleared'})


class MakeOrderAPIView(APIView):
    def get(self, request):
        cart = request.session.get('cart', [])
        print(cart)
        if cart:
            items = Item.objects.filter(id__in=cart)
            order = Order.objects.create()
            order.items.add(*items)
            print(order)
            line_items = OrderSerializer(order)
            print(json.dumps(line_items.data))
            session = stripe.checkout.Session.create(
                success_url=request.build_absolute_uri(reverse('buy-success')),
                line_items=line_items.data['items'],
                mode="payment",
            )
            return Response({'id': session['id']})
        return Response({'error': 'your cart is empty'})
