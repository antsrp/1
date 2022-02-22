from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/purchase/', views.purchase, name='purchase'),
]