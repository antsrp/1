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



"""class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return self.login

    def created_recently(self):
        return self.create_date >= timezone.now() - datetime.delta(days=7)"""

"""
class Purchase(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    # product = models.ManyToManyField(Product)
    quantity = models.IntegerField(blank=False, null=False, default=None)

    def __str__(self):
        return "%s, %s, %s" % (self.user.username, self.product, self.quantity)
        # return self.user.name


class Order(models.Model):
    # purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    purchase = models.ManyToManyField(Purchase)
    date = models.DateTimeField('date created', default=None)

    def __str__(self):
        return "%s, %s" % (self.purchase, self.date)
"""