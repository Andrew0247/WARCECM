# urls en la app de registro de empleados 

from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome_empleado, name="empleado"),
    path('actualizar_empleado/<int:pk>', views.ActualizarEmpleado.as_view(), name="actualizar_empleado"),
    path('registro_empleado/', views.registro_empleados),
    path('listar_contratacion/', views.ContratacionList , name="listar_contratacion"),
    path('crear_contratacion/', views.CrearContratacion.as_view() , name="crear_contratacion"),
    path('actualizar_contratacion/<int:pk>', views.ActualizarContratacion.as_view() , name="actualizar_contratacion"),
    path('listar_educacion/', views.EducacionList , name="listar_educacion"),
    path('crear_educacion/', views.CrearEducacion.as_view() , name="crear_educacion"),
    path('actualizar_educacion/<int:pk>', views.ActualizarEducacion.as_view() , name="actualizar_educacion"),
    path('eliminar_educacion/<int:pk>', views.EliminarEducacion.as_view() , name="eliminar_educacion"),
    path('listar_experiencia/', views.ExperienciaList , name="listar_experiencia"),
    path('crear_experiencia/', views.CrearExperiencia.as_view() , name="crear_experiencia"),
    path('actualizar_experiencia/<int:pk>', views.ActualizarExperiencia.as_view() , name="actualizar_experiencia"),
    path('eliminar_experiencia/<int:pk>', views.EliminarExperiencia.as_view() , name="eliminar_experiencia"),
    path('listar_documentosoporte/', views.DocumentoSoporteList , name="listar_documentosoporte"),
    path('crear_documentosoporte/', views.CrearDocumentoSoporte.as_view() , name="crear_documentosoporte"),
    path('actualizar_documentosoporte/<int:pk>', views.ActualizarDocumentoSoporte.as_view() , name="actualizar_documentosoporte"),
    path('eliminar_documentosoporte/<int:pk>', views.EliminarDocumentoSoporte.as_view() , name="eliminar_documentosoporte"),
    path('listar_valoracion/', views.ValoracionList , name="listar_valoracion"),
    path('crear_valoracion/', views.CrearValoracion.as_view() , name="crear_valoracion"),
    path('actualizar_valoracion/<int:pk>', views.ActualizarValoracion.as_view() , name="actualizar_valoracion"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)