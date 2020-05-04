from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from .forms import ContratanteForm, ContratosExternosForm
from REGContracEx.models import Contratante, Contratos_Externos
from django.core.mail import send_mail
from django.conf import settings
import datetime

# Create your views here.

def welcome_admins(request):
    contratantes = Contratante.objects.all()
    contratos_externos = Contratos_Externos.objects.all()
    contexto = {'contratantes': contratantes,'contratos_externos': contratos_externos}
    if contratos_externos:
        for cont in contratos_externos:
            for emple in contratantes:
                #Colocar un contador para ver si no se repiten los envios de correo
                if (datetime.date.today()+datetime.timedelta(days=3))==cont.fech_fin_contrato:
                    messaje = 'El contrato a nombre de'+' '+emple.nom_contratante+', identificado con cédula N°'+' '+emple.cedu_contratante+', esta proximo a vencerse.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list=[emple.email_contratante]
                    send_mail('Contratacion Externa',messaje,email_from,recipient_list)

    return render(request, "listar_contratos_exte.html", contexto)

class CrearContratante(BSModalCreateView):
    template_name='contratante.html'
    form_class=ContratanteForm
    success_url=reverse_lazy('admins')

class ActualizarContratante(BSModalUpdateView):
    model = Contratante
    template_name='contratante.html'
    form_class=ContratanteForm
    success_url=reverse_lazy('admins')

class EliminarContratante(BSModalDeleteView):
    model = Contratante
    template_name = 'contratante_delete.html'
    success_message = 'Hecho. El Contratante Ha Sido Eliminado!!.'
    success_url = reverse_lazy('admins')

class CrearContratoExterno(BSModalCreateView):
    template_name='contrato_externo.html'
    form_class=ContratosExternosForm
    success_url=reverse_lazy('admins')

class ActualizarContratoExterno(BSModalUpdateView):
    model = Contratos_Externos
    template_name='contrato_externo.html'
    form_class=ContratosExternosForm
    success_url=reverse_lazy('admins')

class EliminarContratoExterno(BSModalDeleteView):
    model = Contratos_Externos
    template_name = 'contrato_externo_delete.html'
    success_message = 'Hecho. El Contrato Externo Ha Sido Eliminado!!.'
    success_url = reverse_lazy('admins')