from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, login as do_login, authenticate
from django.contrib.auth.models import Group
from REGEmpleados.views import registro_empleados, welcome_empleado
from REGContracEx.views import welcome_admins
# Integrando el nuevo AuthenticationForm
from .forms import UserForm, UserCreateForm, UserAdminForm, UserAdminCreateForm

# Create your views here.

def welcome(request):
    if request.user.groups.filter(name='Contratos_Externos').exists():
        return redirect('/contratos_externos/')
    elif request.user.groups.filter(name='Jefes_Secretaria').exists():
        return redirect('/jefes_empleados/')
    elif request.user.groups.filter(name='Empleados').exists():
        return redirect('/empleados/')
    elif request.user.is_authenticated:
        return redirect('/empleados/')
    return redirect('login/')

def register(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                if 'grupo' in request.POST:
                    if request.POST['grupo'] == "1":
                        grupo = Group.objects.get(name='Contratos_Externos')
                        grupo.user_set.add(user)
                        return redirect('/contratos_externos/')
                    if request.POST['grupo'] == "2":
                        grupo = Group.objects.get(name='Jefes_Secretaria')
                        grupo.user_set.add(user)
                        return redirect('/jefes_empleados/registro_jefes/')
                    if request.POST['grupo'] == "3":
                        grupo = Group.objects.get(name='Empleados')
                        grupo.user_set.add(user)
                        return redirect('/empleados/registro_empleado/')

    return render(request, "register.html", {'form': form})

def login(request):
    form = UserForm()
    form2 = UserAdminForm()
    
    if 'usuarios' in request.POST:
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/usuarios/')

    elif 'admins' in request.POST:
        form2 = UserAdminForm(data=request.POST)
        if form2.is_valid():
            username = form2.cleaned_data['username']
            password = form2.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/usuarios/')

    return render(request, "login.html", {'form': form,'form2':form2})

def logout(request):
    do_logout(request)
    return redirect('/usuarios/')