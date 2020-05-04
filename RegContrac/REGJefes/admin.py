from django.contrib import admin
from REGJefes.models import Jefe,Contratacion,Educacion,Experiencia_Laboral,Documentos_Soporte,ValoracionJefe

# Register your models here.
class Media:
    js = (
        '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
        #'js/admin.js',       # project static folder
    )

class JefeAdmin(admin.ModelAdmin):
    list_display=("nom_jefe", "ape_jefe", "cedu_jefe", "email_jefe", "estado_jefe")
    search_fields=("nom_jefe", "ape_jefe", "estado_jefe")
    list_filter=('estado_jefe','cedu_jefe')

class ContratacionAdmin(admin.ModelAdmin):
    list_display=("cargo_empleado","tipo_contrato","contrato_doc", "fech_inicio_contrato", "fech_fin_contrato",)
    search_fields=("desc_cargo_empleado","tipo_contrato",)
    date_hierarchy="fech_inicio_contrato"
    list_filter = ('fech_fin_contrato','tipo_contrato')

class EducacionAdmin(admin.ModelAdmin):
    list_display=("nom_instituto", "niv_educativo", "deta_educacion", "cursa_educacion","fech_inicio_edu","fech_fin_edu",)
    search_fields=("nom_instituto", "niv_educacion", "cursa_educacion")
    date_hierarchy="fech_inicio_edu"
    list_filter=('fech_fin_edu','niv_educativo')

class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display=("nom_empresa", "cargo_experiencia", "dura_experiencia","certificacion_labo","fech_inicio_expe","fech_fin_expe")
    search_fields=("nom_empresa","dura_experiencia")
    date_hierarchy="fech_inicio_expe"
    list_filter=('dura_experiencia','fech_fin_expe','fech_inicio_expe')

class Documentos_SoporteAdmin(admin.ModelAdmin):
    list_display=("tipo_documento","documento_soporte",)
    search_fields=("tipo_documento",)
    list_filter=('tipo_documento',)

class ValoracionJefeAdmin(admin.ModelAdmin):
    list_display=("valoracion", "observacion")
    search_fields=("valoracion",)
    list_filter=('valoracion',)

admin.site.register(Jefe, JefeAdmin)
admin.site.register(Contratacion, ContratacionAdmin)
admin.site.register(Educacion, EducacionAdmin)
admin.site.register(Experiencia_Laboral, ExperienciaLaboralAdmin)
admin.site.register(Documentos_Soporte, Documentos_SoporteAdmin)
admin.site.register(ValoracionJefe, ValoracionJefeAdmin)