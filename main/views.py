from django.shortcuts import render
from django.urls import reverse
from .models import Item
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config


stripe.api_key = config('STRIPE_KEY')
# Create your views here.


def item_retrieve(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item.html', {'item': item})


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