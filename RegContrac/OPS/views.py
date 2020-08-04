from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from REGEmpleados.models import Empleado, Contratacion, Educacion, Experiencia_Laboral, Documentos_Soporte, Valoracion

numero=[]

def welcome_ops(request):
    empleados = Empleado.objects.all()
    contras = Contratacion.objects.all()
    num=len(empleados)
    for j in range(num):
        nume=j+1
        numero.append(nume)
    contexto = {'empleados': empleados, 'contratacion':contras,'nume':numero}

    return render(request, "ops_listar.html", contexto)