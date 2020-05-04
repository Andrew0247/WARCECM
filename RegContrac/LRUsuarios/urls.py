# urls en la app de registro de usuarios

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]