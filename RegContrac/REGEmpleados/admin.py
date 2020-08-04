from django.contrib import admin
from REGEmpleados.models import Empleado,Contratacion,Educacion,Experiencia_Laboral,Documentos_Soporte,Valoracion

# Register your models here.
class Media:
    js = (
        '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
        #'js/admin.js',       # project static folder
    )

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=("nom_empleado", "ape_empleado", "cedu_empleado", "email_empleado", "estado_empleado")
    search_fields=("nom_empleado", "ape_empleado", "estado_empleado")
    list_filter=('estado_empleado','cedu_empleado')

class ContratacionAdmin(admin.ModelAdmin):
    list_display=("empleado","objeto_contrato","clase_contrato","valor_contrato", "contrato_doc", "dura_contrato", "fech_inicio_contrato", "fech_fin_contrato", "supervisor",)
    search_fields=("empleado","objeto_contrato","clase_contrao",)
    date_hierarchy="fech_inicio_contrato"
    list_filter = ('supervisor','fech_fin_contrato','objeto_contrato')

class EducacionAdmin(admin.ModelAdmin):
    list_display=("empleado","nom_instituto", "niv_educativo", "deta_educacion", "cursa_educacion","fech_inicio_edu","fech_fin_edu",)
    search_fields=("nom_instituto", "niv_educacion", "cursa_educacion")
    date_hierarchy="fech_inicio_edu"
    list_filter=('fech_fin_edu','niv_educativo')

class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display=("empleado","nom_empresa", "cargo_experiencia", "dura_experiencia","certificacion_labo","fech_inicio_expe","fech_fin_expe")
    search_fields=("nom_empresa","dura_experiencia")
    date_hierarchy="fech_inicio_expe"
    list_filter=('dura_experiencia','fech_fin_expe','fech_inicio_expe')

class Documentos_SoporteAdmin(admin.ModelAdmin):
    list_display=("empleado","tipo_documento","documento_soporte",)
    search_fields=("tipo_documento",)
    list_filter=('tipo_documento',)

class ValoracionAdmin(admin.ModelAdmin):
    list_display=("empleado","valoracion", "observacion")
    search_fields=("valoracion",)
    list_filter=('valoracion',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Contratacion, ContratacionAdmin)
admin.site.register(Educacion, EducacionAdmin)
admin.site.register(Experiencia_Laboral, ExperienciaLaboralAdmin)
admin.site.register(Documentos_Soporte, Documentos_SoporteAdmin)
admin.site.register(Valoracion, ValoracionAdmin)