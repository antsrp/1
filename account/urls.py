import django.contrib.auth.views as djangoviews
from django.urls import path

from . import views

urlpatterns = [
    path('logout/', djangoviews.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('success/', views.success_registration, name='success'),
    path('register/', views.registration, name='register'),
    path('signin/', views.signin, name='signin'),
]