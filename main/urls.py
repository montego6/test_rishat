from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.item_retrieve, name='item-retrieve')
]