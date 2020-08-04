from django import forms
from django.forms import ModelForm
from bootstrap_modal_forms.forms import BSModalForm # Se intalo bootstrap_modal_forms con django-bootstrap-modal-forms
from REGEmpleados.models import Empleado, Contratacion, Educacion, Experiencia_Laboral, Documentos_Soporte, Valoracion

class EmpleadoForm(ModelForm):
    nom_empleado = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    ape_empleado = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    cedu_empleado = forms.CharField(label="Cedula", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}))
    celu_empleado = forms.CharField(label="Celular", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}))
    email_empleado = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado_empleado'].widget.attrs.update({'class':'custom-control-input'})

    class Meta:
        model = Empleado
        fields = ['nom_empleado', 'ape_empleado', 'cedu_empleado', 'celu_empleado', 'email_empleado', 'estado_empleado']

class Empleado2Form(BSModalForm):
    nom_empleado = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    ape_empleado = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    cedu_empleado = forms.CharField(label="Cedula", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}))
    celu_empleado = forms.CharField(label="Celular", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}))
    email_empleado = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['estado_empleado'].widget.attrs.update({'class':'custom-control-input'})

    class Meta:
        model = Empleado
        fields = ['nom_empleado', 'ape_empleado', 'cedu_empleado', 'celu_empleado', 'email_empleado']

class ContratacionForm(BSModalForm):
    class Meta:
        model = Contratacion
        fields = ['empleado','objeto_contrato','clase_contrato','valor_contrato', 'contrato_doc', 'dura_contrato', 'fech_inicio_contrato', 'fech_fin_contrato', 'supervisor']
    
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

class ValoracionForm(BSModalForm):
    class Meta:
        model = Valoracion
        fields = ['empleado','valoracion', 'observacion']
    
    def __init__(self, *args, **kwargs):
        super(ValoracionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })