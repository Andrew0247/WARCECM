from django.contrib import admin
from REGContracEx.models import Contratante, Contratos_Externos

# Register your models here.

class Media:
    js = (
        '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
        #'js/admin.js',       # project static folder
    )

class ContratanteAdmin(admin.ModelAdmin):
    list_display=("nom_contratante", "ape_contratante", "cedu_contratante", "celu_contratante", "email_contratante")
    search_fields=("nom_contratante", "ape_contratante", "cedu_contratante")
    list_filter=('nom_contratante','cedu_contratante')

class ContratosExternosAdmin(admin.ModelAdmin):
    list_display=("tipo_contrato","objeto_contrato","doc_contrato", "fech_inicio_contrato", "fech_fin_contrato",)
    search_fields=("tipo_contrato","objeto_contrato",)
    date_hierarchy="fech_inicio_contrato"
    list_filter = ('fech_fin_contrato','tipo_contrato','objeto_contrato')

admin.site.register(Contratante, ContratanteAdmin)
admin.site.register(Contratos_Externos, ContratosExternosAdmin)