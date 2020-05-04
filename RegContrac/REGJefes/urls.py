# urls en la app de registro de jefes

from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome_jefe, name="jefe"),
    path('registro_jefes/', views.registro_jefes, name="registro_jefes"),
    path('actualizar_jefe/<int:pk>', views.ActualizarJefe.as_view(), name="actualizar_jefe"),
    path('listar_contratacion_jefe/', views.ContratacionJefeList , name="listar_contratacion_jefe"),
    path('crear_contratacion_jefe/', views.CrearContratacionJefe.as_view() , name="crear_contratacion_jefe"),
    path('actualizar_contratacion_jefe/<int:pk>', views.ActualizarContratacionJefe.as_view() , name="actualizar_contratacion_jefe"),
    path('listar_educacion_jefe/', views.EducacionJefeList , name="listar_educacion_jefe"),
    path('crear_educacion_jefe/', views.CrearEducacionJefe.as_view() , name="crear_educacion_jefe"),
    path('actualizar_educacion_jefe/<int:pk>', views.ActualizarEducacionJefe.as_view() , name="actualizar_educacion_jefe"),
    path('eliminar_educacion_jefe/<int:pk>', views.EliminarEducacionJefe.as_view() , name="eliminar_educacion_jefe"),
    path('listar_experiencia_jefe/', views.ExperienciaJefeList , name="listar_experiencia_jefe"),
    path('crear_experiencia_jefe/', views.CrearExperienciaJefe.as_view() , name="crear_experiencia_jefe"),
    path('actualizar_experiencia_jefe/<int:pk>', views.ActualizarExperienciaJefe.as_view() , name="actualizar_experiencia_jefe"),
    path('eliminar_experiencia_jefe/<int:pk>', views.EliminarExperienciaJefe.as_view() , name="eliminar_experiencia_jefe"),
    path('listar_documentosoporte_jefe/', views.DocumentoSoporteJefeList , name="listar_documentosoporte_jefe"),
    path('crear_documentosoporte_jefe/', views.CrearDocumentoSoporteJefe.as_view() , name="crear_documentosoporte_jefe"),
    path('actualizar_documentosoporte_jefe/<int:pk>', views.ActualizarDocumentoSoporteJefe.as_view() , name="actualizar_documentosoporte_jefe"),
    path('eliminar_documentosoporte_jefe/<int:pk>', views.EliminarDocumentoSoporteJefe.as_view() , name="eliminar_documentosoporte_jefe"),
    path('listar_valoracion_jefe/', views.ValoracionJefeList , name="listar_valoracion_jefe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)