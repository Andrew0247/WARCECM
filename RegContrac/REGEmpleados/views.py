from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from .forms import EmpleadoForm, Empleado2Form, ContratacionForm, EducacionForm, Experiencia_LaboralForm, Documentos_SoporteForm, ValoracionForm
from REGEmpleados.models import Empleado, Contratacion, Educacion, Experiencia_Laboral, Documentos_Soporte, Valoracion
# from REGJefes.views import ValoracionJefeList
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import datetime

# Create your views here.

def registro_empleados(request):
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('/empleados/')

    return render(request, "registro_empleados.html", {'form': form})

def welcome_empleado(request):
    empleados = Empleado.objects.all()
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

    return render(request, "panel_empleados.html", contexto)

class ActualizarEmpleado(BSModalUpdateView):
    model = Empleado
    template_name='empleado.html'
    form_class=Empleado2Form
    success_url=reverse_lazy('empleado')

def ContratacionList(request):
    empleados = Empleado.objects.all()
    contracion = Contratacion.objects.all()
    # for emple in empleados:
    #     user = User.objects.get(username=emple.cedu_empleado)
    #     if user.get_all_permissions():
    #         if user.has_perms(['REGEmpleados.view_contratacion']):
    contexto = {'empleados':empleados,'contratacion':contracion}
    return render(request,"contratacion_empleados.html", contexto)

class CrearContratacion(BSModalCreateView):
    template_name='contratacion.html'
    form_class=ContratacionForm
    success_url=reverse_lazy('listar_contratacion')

class ActualizarContratacion(BSModalUpdateView):
    model = Contratacion
    template_name='contratacion.html'
    form_class=ContratacionForm
    success_url=reverse_lazy('listar_contratacion')

def EducacionList(request):
    empleados = Empleado.objects.all()
    educacion = Educacion.objects.all()
    contexto = {'empleados':empleados,'educacion':educacion}
    return render(request,"educacion_empleados.html", contexto)

class CrearEducacion(BSModalCreateView):
    template_name='educacion.html'
    form_class=EducacionForm
    success_url=reverse_lazy('listar_educacion')

class ActualizarEducacion(BSModalUpdateView):
    model = Educacion
    template_name='educacion.html'
    form_class=EducacionForm
    success_url=reverse_lazy('listar_educacion')

class EliminarEducacion(BSModalDeleteView):
    model = Educacion
    template_name = 'educacion_delete.html'
    success_message = 'Hecho. El Item Ha Sido Eliminado!!.'
    success_url = reverse_lazy('listar_educacion')

#======= Añadir el Delete para Educacion, Experiencia y Documentos Soporte ===========
def ExperienciaList(request):
    empleados = Empleado.objects.all()
    experiencia = Experiencia_Laboral.objects.all()
    contexto = {'empleados':empleados,'experiencia_labo':experiencia}
    return render(request,"experiencia_empleados.html", contexto)

class CrearExperiencia(BSModalCreateView):
    template_name='experiencia.html'
    form_class=Experiencia_LaboralForm
    success_url=reverse_lazy('listar_experiencia')

class ActualizarExperiencia(BSModalUpdateView):
    model = Experiencia_Laboral
    template_name='experiencia.html'
    form_class=Experiencia_LaboralForm
    success_url=reverse_lazy('listar_experiencia')

class EliminarExperiencia(BSModalDeleteView):
    model = Experiencia_Laboral
    template_name = 'experiencia_delete.html'
    success_message = 'Hecho. El Item Ha Sido Eliminado!!.'
    success_url = reverse_lazy('listar_experiencia')

def DocumentoSoporteList(request):
    empleados = Empleado.objects.all()
    documentoS = Documentos_Soporte.objects.all()
    contexto = {'empleados':empleados,'documentos_soporte':documentoS}
    return render(request,"documentoS_empleados.html", contexto)

class CrearDocumentoSoporte(BSModalCreateView):
    template_name='documento_soporte.html'
    form_class=Documentos_SoporteForm
    success_url=reverse_lazy('listar_documentosoporte')

class ActualizarDocumentoSoporte(BSModalUpdateView):
    model = Documentos_Soporte
    template_name='documento_soporte.html'
    form_class=Documentos_SoporteForm
    success_url=reverse_lazy('listar_documentosoporte')

class EliminarDocumentoSoporte(BSModalDeleteView):
    model = Documentos_Soporte
    template_name = 'documentosop_delete.html'
    success_message = 'Hecho. El Item Ha Sido Eliminado!!.'
    success_url = reverse_lazy('listar_documentosoporte')

def ValoracionList(request):
    empleados = Empleado.objects.all()
    valora = Valoracion.objects.all()
    contexto = {'empleados':empleados,'valoraciones':valora}
    return render(request,"valoracion_empleados.html", contexto)

class CrearValoracion(BSModalCreateView):
    template_name='valoracion.html'
    form_class=ValoracionForm
    success_url=reverse_lazy('listar_valoracion_jefe')

class ActualizarValoracion(BSModalUpdateView):
    model = Valoracion
    template_name='valoracion.html'
    form_class=ValoracionForm
    success_url=reverse_lazy('listar_valoracion_jefe')