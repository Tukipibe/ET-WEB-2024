from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro",[])
    total = 0
    for item in carro:
        total += item[4]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[2]
        detalle.cantidad = item[3]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []
    return redirect(to="carrito")

    
def carrito(request):
    return render(request, 'carrito.html', {"carro":request.session.get("carro",[])})

def home(request):
    libros = Producto.objects.all
    return render(request, 'index.html', {'libros':libros, "carro":request.session.get("carro",[])})

def login(request):
    return render(request, 'login.html')

def logout(request):
    return logout_then_login(request,login_url= 'login')

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'registro.html', {'form':registro})

def venta(request):
    return render(request, 'top_ventas.html')

def formu(request):
    return render(request, 'formulario.html')

def recom(request):
    return render(request, 'recomendaciones.html')


def addtocar(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro",[])
    for item in carro:
        if item[0] == codigo:
            item[3] +=1
            item[4] = item[2] * item[3]
            break
    else:
        carro.append([codigo, producto.nombre, producto.precio, 1,producto.precio, producto.imagen])
    request.session["carro"] = carro
    return redirect(to="home")

def dropitem(request,codigo):
    carro = request.session.get("carro",[])
    for item in carro:
        if item[0] == codigo:
            if item[3]>1:
                item[3] -=1
                item[4] = item[2] * item[3]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")