import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField('date created')

    def __str__(self):
        return "%s %s %s" % (self.id, self.user.username, self.date)


class Purchase(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    # product = models.ManyToManyField(Product)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None)
    quantity = models.IntegerField(default=None)

    def __str__(self):
        return "%s %s %s" % (self.order, self.product, self.quantity)

