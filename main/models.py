from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.price}'
