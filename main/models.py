from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_buy_url(self):
        return reverse('buy-item', kwargs={'id': self.id})
