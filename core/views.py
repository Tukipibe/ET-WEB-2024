import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.conf import settings
from django.http import JsonResponse

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
    
def analyze_recipe(request):
     if request.method == 'POST':
        # Recibe los datos de la receta desde la solicitud POST
        ingredients = request.POST.getlist('ingredients[]')  # lista de ingredientes

        # Prepara los datos para enviarlos a la API de Edamam
        url = 'https://api.edamam.com/api/nutrition-details'
        headers = {'Content-Type': 'application/json'}
        data = {
            "title": "Análisis Nutricional",
            "ingr": ingredients
        }
        
        # Parámetros de autenticación
        params = {
            'app_id': settings.EDAMAM_APP_ID,
            'app_key': settings.EDAMAM_APP_KEY
        }

        # Realiza la solicitud a la API de Edamam
        response = requests.post(url, json=data, headers=headers, params=params)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            nutrition_data = response.json()
            return JsonResponse(nutrition_data)  # Devuelve los datos en formato JSON
        else:
            return JsonResponse({'error': 'No se pudo analizar la receta.'}, status=400)
     else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)