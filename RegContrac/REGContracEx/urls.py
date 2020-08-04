# urls en la app de contratos externos

from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome_admins, name="admins"),
    path('crear_contratante/', views.CrearContratante.as_view() , name="crear_contratante"),
    path('actualizar_contratante/<int:pk>', views.ActualizarContratante.as_view() , name="actualizar_contratante"),
    path('eliminar_contratante/<int:pk>', views.EliminarContratante.as_view() , name="eliminar_contratante"),
    path('crear_contrato_externo/', views.CrearContratoExterno.as_view() , name="crear_contrato_externo"),
    path('actualizar_contrato_externo/<int:pk>', views.ActualizarContratoExterno.as_view() , name="actualizar_contrato_externo"),
    path('eliminar_contrato_externo/<int:pk>', views.EliminarContratoExterno.as_view() , name="eliminar_contrato_externo"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)