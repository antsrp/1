from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import *
from datetime import *

import json


def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'auth': request.user.is_authenticated
    }
    return render(request, 'products/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")


def purchase(request, product_id):
    return HttpResponse("You're purchasing product %s." % product_id)


def create_order(request):
    order = request.body.decode('utf-8')
    lul = json.loads(request.body)
    date = datetime.now()
    o = Order(user=request.user, date=date)
    o.save()
    for p in lul:
        prod = Product.objects.get(id=p['id'])
        quantity = p['quantity']
        pur = Purchase(order=o, product=prod, quantity=quantity)
        pur.save()
    # kek = lul[0]['id']
    return HttpResponse("You're just ordered something!")
    # return redirect('dashboard')