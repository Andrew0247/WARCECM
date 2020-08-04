# urls en la app de registro de usuarios

from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.welcome, name="usuario"),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)