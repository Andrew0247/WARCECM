# urls en la app de listar OPS 

from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.

urlpatterns = [
    path('', views.welcome_ops, name="ops"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)