from django import forms
from django.forms import ModelForm
from bootstrap_modal_forms.forms import BSModalForm # Se intalo bootstrap_modal_forms con django-bootstrap-modal-forms
from .models import Jefe, Contratacion, Educacion, Experiencia_Laboral, Documentos_Soporte, ValoracionJefe

class JefeForm(ModelForm):
    nom_jefe = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    ape_jefe = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    cedu_jefe = forms.CharField(label="Cedula", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}))
    celu_jefe = forms.CharField(label="Celular", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}))
    email_jefe = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado_jefe'].widget.attrs.update({'class':'custom-control-input'})

    class Meta:
        model = Jefe
        fields = ['nom_jefe', 'ape_jefe', 'cedu_jefe', 'celu_jefe', 'email_jefe', 'estado_jefe']

class Jefe2Form(BSModalForm):
    nom_jefe = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    ape_jefe = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    cedu_jefe = forms.CharField(label="Cedula", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}))
    celu_jefe = forms.CharField(label="Celular", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}))
    email_jefe = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['estado_empleado'].widget.attrs.update({'class':'custom-control-input'})

    class Meta:
        model = Jefe
        fields = ['nom_jefe', 'ape_jefe', 'cedu_jefe', 'celu_jefe', 'email_jefe']

class ContratacionForm(BSModalForm):
    class Meta:
        model = Contratacion
        fields = ['empleado','cargo_empleado','tipo_contrato','contrato_doc', 'fech_inicio_contrato', 'fech_fin_contrato']
    
    def __init__(self, *args, **kwargs):
        super(ContratacionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fech_inicio_contrato'].widget.attrs.update({'id':'datetimepicker'})
        self.fields['fech_fin_contrato'].widget.attrs.update({'id':'datetimepicker2'})

class EducacionForm(BSModalForm):
    class Meta:
        model = Educacion
        fields = ['empleado','nom_instituto', 'niv_educativo', 'deta_educacion', 'cursa_educacion', 'fech_inicio_edu', 'fech_fin_edu']

    def __init__(self, *args, **kwargs):
        super(EducacionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fech_inicio_edu'].widget.attrs.update({'id':'datetimepicker'})
        self.fields['fech_fin_edu'].widget.attrs.update({'id':'datetimepicker2'})

class Experiencia_LaboralForm(BSModalForm):
    class Meta:
        model = Experiencia_Laboral
        fields = ['empleado','nom_empresa', 'cargo_experiencia', 'dura_experiencia','certificacion_labo','fech_inicio_expe', 'fech_fin_expe']
    
    def __init__(self, *args, **kwargs):
        super(Experiencia_LaboralForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fech_inicio_expe'].widget.attrs.update({'id':'datetimepicker'})
        self.fields['fech_fin_expe'].widget.attrs.update({'id':'datetimepicker2'})

class Documentos_SoporteForm(BSModalForm):
    class Meta:
        model = Documentos_Soporte
        fields = ['empleado','tipo_documento','documento_soporte']

    def __init__(self, *args, **kwargs):
        super(Documentos_SoporteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ValoracionJefeForm(BSModalForm):
    class Meta:
        model = ValoracionJefe
        fields = ['empleado','valoracion', 'observacion']
    
    def __init__(self, *args, **kwargs):
        super(ValoracionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })