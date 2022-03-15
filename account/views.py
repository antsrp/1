from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import FieldDoesNotExist

from .forms import LoginForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from store.models import *

@login_required
def dashboard(request):
    orders = Order.objects.filter(user_id=request.user.id)
    purchases = Purchase.objects.select_related('order', 'product').filter(order__user_id=request.user.id)
    if not orders:
        orders = None
    if not purchases:
        purchases = None
    context = {
        'section': 'dashboard',
        'orders': orders,
        'purchases' : purchases
    }
    return render(request, 'account/dashboard.html',  context)


def registration(request):
    error = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.cleaned_data is not None:
            username = form.cleaned_data.get('username')
            # pass1 = form.cleaned_data.get('password1')
            # pass2 = form.cleaned_data.get('password2')

        pass1 = form.data['password1']
        pass2 = form.data['password2']

        if pass1 == pass2:
            if username is not None:
                User.objects.create_user(username=username,
                                         password=pass1)
                request.session['page_from_redirect'] = True
                return redirect('success')
            else:
                error = "user"
        else:
            error = "pass"
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
    return render(request, 'account/custom_signup.html', {'section': 'signup', 'error': error})


def get_user_by_username(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return False


def get_orders_by_id(id):
    try:
        return Order.objects.filter(user_id=id)
    except Order.DoesNotExist:
        return False


def signin(request):
    error = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # if form.is_valid():
        cd = form.data
        username = cd['username']
        passw = cd['password1']
        # cd = form.cleaned_data
        obj = get_user_by_username(username)
        if not obj:
            error = "user"
        else:
            user = authenticate(username=username, password=passw)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error = "account disabled"
            else:
                error = "pass"
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
    return render(request, 'account/custom_login.html', {'section': 'signin', 'error': error})


def success_registration(request):
    if 'page_from_redirect' in request.session:
        return render(request, 'account/aftersignup.html')
    else:
        return redirect('signup')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            request.session['page_from_redirect'] = True
            return redirect('success')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form, 'section': 'signup'})
