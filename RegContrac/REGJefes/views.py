from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from REGJefes.forms import JefeForm, Jefe2Form, ContratacionForm, EducacionForm, Experiencia_LaboralForm, Documentos_SoporteForm, ValoracionJefeForm
from REGJefes.models import Jefe, Contratacion, Educacion, Experiencia_Laboral, Documentos_Soporte
from REGEmpleados.models import Empleado, Valoracion
from django.core.mail import send_mail
from django.conf import settings
import datetime

# Create your views here.

def registro_jefes(request):
    form = JefeForm()
    if request.method == "POST":
        form = JefeForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('/jefes_empleados/')

    return render(request, "registro_jefes.html", {'form': form})

def welcome_jefe(request):
    empleados = Jefe.objects.all()
    contexto = {'empleados': empleados}
    contras = Contratacion.objects.all()
    if contras:
        for cont in contras:
            for emple in empleados:
                #Colocar un contador para ver si no se repiten los envios de correo
                if (datetime.date.today()+datetime.timedelta(days=3))==cont.fech_fin_contrato:
                    messaje = 'Señor(a), identificado con cédula'+' '+emple.cedu_empleado+', su contrato esta proximo a vencerse.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list=[emple.email_empleado]
                    send_mail('Contratacion',messaje,email_from,recipient_list)

    return render(request, "panel_jefes.html", contexto)

class ActualizarJefe(BSModalUpdateView):
    model = Jefe
    template_name='jefe.html'
    form_class=Jefe2Form
    success_url=reverse_lazy('jefe')

def ContratacionJefeList(request):
    empleados = Jefe.objects.all()
    contracion = Contratacion.objects.all().select_related('empleado')
    contexto = {'empleados':empleados,'contratacion':contracion}
    return render(request,"contratacion_jefes.html", contexto)

class CrearContratacionJefe(BSModalCreateView):
    template_name='contratacion_jef.html'
    form_class=ContratacionForm
    success_url=reverse_lazy('listar_contratacion_jefe')

class ActualizarContratacionJefe(BSModalUpdateView):
    model = Contratacion
    template_name='contratacion_jef.html'
    form_class=ContratacionForm
    success_url=reverse_lazy('listar_contratacion_jefe')

def EducacionJefeList(request):
    empleados = Jefe.objects.all()
    educacion = Educacion.objects.all().select_related('empleado')
    contexto = {'empleados':empleados,'educacion':educacion}
    return render(request,"educacion_jefes.html", contexto)

class CrearEducacionJefe(BSModalCreateView):
    template_name='educacion_jef.html'
    form_class=EducacionForm
    success_url=reverse_lazy('listar_educacion_jefe')

class ActualizarEducacionJefe(BSModalUpdateView):
    model = Educacion
    template_name='educacion_jef.html'
    form_class=EducacionForm
    success_url=reverse_lazy('listar_educacion_jefe')

class EliminarEducacionJefe(BSModalDeleteView):
    model = Educacion
    template_name = 'educacion_delete_jef.html'
    success_message = 'Hecho. El Item Ha Sido Eliminado!!.'
    success_url = reverse_lazy('listar_educacion_jefe')

#======= Añadir el Delete para Educacion, Experiencia y Documentos Soporte ===========
def ExperienciaJefeList(request):
    empleados = Jefe.objects.all()
    experiencia = Experiencia_Laboral.objects.all().select_related('empleado')
    contexto = {'empleados':empleados,'experiencia_labo':experiencia}
    return render(request,"experiencia_jefes.html", contexto)

class CrearExperienciaJefe(BSModalCreateView):
    template_name='experiencia_jef.html'
    form_class=Experiencia_LaboralForm
    success_url=reverse_lazy('listar_experiencia_jefe')

class ActualizarExperienciaJefe(BSModalUpdateView):
    model = Experiencia_Laboral
    template_name='experiencia_jef.html'
    form_class=Experiencia_LaboralForm
    success_url=reverse_lazy('listar_experiencia_jefe')

class EliminarExperienciaJefe(BSModalDeleteView):
    model = Experiencia_Laboral
    template_name = 'experiencia_delete_jef.html'
    success_message = 'Hecho. El Item Ha Sido Eliminado!!.'
    success_url = reverse_lazy('listar_experiencia_jefe')

def DocumentoSoporteJefeList(request):
    empleados = Jefe.objects.all()
    documentoS = Documentos_Soporte.objects.all().select_related('empleado')
    contexto = {'empleados':empleados,'documentos_soporte':documentoS}
    return render(request,"documentoS_jefes.html", contexto)

class CrearDocumentoSoporteJefe(BSModalCreateView):
    template_name='documento_soporte_jef.html'
    form_class=Documentos_SoporteForm
    success_url=reverse_lazy('listar_documentosoporte_jefe')

class ActualizarDocumentoSoporteJefe(BSModalUpdateView):
    model = Documentos_Soporte
    template_name='documento_soporte_jef.html'
    form_class=Documentos_SoporteForm
    success_url=reverse_lazy('listar_documentosoporte_jefe')

class EliminarDocumentoSoporteJefe(BSModalDeleteView):
    model = Documentos_Soporte
    template_name = 'documentosop_delete_jef.html'
    success_message = 'Hecho. El Item Ha Sido Eliminado!!.'
    success_url = reverse_lazy('listar_documentosoporte_jefe')

#========== Creo que se debe modificar el reverse_lazy ======
def ValoracionJefeList(request):
    empleados = Empleado.objects.all()
    jefe = Jefe.objects.all()
    valora = Valoracion.objects.all()
    contexto = {'empleados':jefe,'valoraciones':valora,'empleados1':empleados}
    return render(request,"valoracion_jefes.html", contexto)
