import django.contrib.auth.views as djangoviews
from django.urls import path

from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # path('login/', 'django.contrib.auth.views.login', name='login'),
    # path('logout/', 'django.contrib.auth.views.logout', name='logout'),
    path('login/', djangoviews.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', djangoviews.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    # path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
]