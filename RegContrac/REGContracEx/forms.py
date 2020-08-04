from django import forms
from django.forms import ModelForm
from bootstrap_modal_forms.forms import BSModalForm # Se intalo bootstrap_modal_forms con django-bootstrap-modal-forms
from REGContracEx.models import Contratante, Contratos_Externos

class ContratanteForm(BSModalForm):
    class Meta:
        model = Contratante
        fields = ['nom_contratante','ape_contratante','cedu_contratante', 'celu_contratante', 'email_contratante']
    
    def __init__(self, *args, **kwargs):
        super(ContratanteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ContratosExternosForm(BSModalForm):
    class Meta:
        model = Contratos_Externos
        fields = ['contratante','clase_contrato','objeto_contrato','doc_contrato', 'fech_inicio_contrato', 'fech_fin_contrato', 'supervisor']
    
    def __init__(self, *args, **kwargs):
        super(ContratosExternosForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fech_inicio_contrato'].widget.attrs.update({'id':'datetimepicker'})
        self.fields['fech_fin_contrato'].widget.attrs.update({'id':'datetimepicker2'})