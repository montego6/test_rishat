from django.shortcuts import render
from django.urls import reverse
from .models import Item
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response


stripe.api_key = "pk_test_51McWQcDlPs5u4HwiXU90HVvWjuDJjOPFOoQV35sWS44HHELoefCrjSoHdRN4hRfoLfmsZkxSARDuRF4Q412znY0d00t6YkA4M7"
# Create your views here.
# pk_test_a9nwZVa5O7b0xz3lxl318KSU00x1L9ZWsF

def item_retrieve(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item.html', {'item': item})


def buy_success(request):
    return render(request, 'success.html')


class BuyItemAPIView(APIView):

    def get(self, request, id):
        item = Item.objects.get(id=id)
        product = stripe.Product.create(name=item.name)
        price = stripe.Price.create(
                                      unit_amount=int(item.price*100),
                                      currency="usd",
                                      product=product['id'],
                                    )
        session = stripe.checkout.Session.create(
            success_url=reverse('buy-success'),
            line_items=[
                {
                    "price": price['id'],
                    "quantity": 1,
                },
            ],
            mode="payment",
        )
        return Response({'session_id': session['id']})