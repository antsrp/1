from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Product


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
    kek = 0
    return HttpResponse("You're just ordered something!" )
    #return redirect('dashboard')