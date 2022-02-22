import datetime
from django.utils import timezone
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name


class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return self.login

    def created_recently(self):
        return self.create_date >= timezone.now() - datetime.delta(days=7)


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Order(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def __str__(self):
        return self.purchase
