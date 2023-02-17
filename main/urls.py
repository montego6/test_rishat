from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', views.item_retrieve, name='item-retrieve'),
    path('buy/<int:id>/', views.BuyItemAPIView.as_view(), name='buy-item'),
    path('buy/success/', views.buy_success, name='buy-success'),
]