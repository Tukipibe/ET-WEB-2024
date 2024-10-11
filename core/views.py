from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *

def home(request):
    return render(request,'index.html')

def inicio(request):
    return render(request,'inicio.html')

def nosotros(request):
    return render(request,'nosotros.html')

def proyectos(request):
    return render(request,'proyectos.html')

def contactos(request):
    return render(request,'contactos.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,login_url='login')

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
        else:
            registro = Registro()
        return render(request, 'registro.html',{'form':registro})