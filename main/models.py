from django.db import models
from django.urls import reverse
import stripe
from decouple import config

stripe.api_key = config('STRIPE_KEY')


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        product = stripe.Product.create(name=self.name)
        price = stripe.Price.create(
            unit_amount=int(self.price * 100),
            currency="usd",
            product=product['id'],
        )
        StripeItem.objects.create(item=self, product=product['id'], price=price['id'])

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_buy_url(self):
        return reverse('buy-item', kwargs={'id': self.id})


class StripeItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='stripe')
    product = models.CharField(max_length=300)
    price = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.item.name} - {self.item.price}'
