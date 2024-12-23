import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .data import carbon_footprint_data

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
    django_logout(request)
    return redirect('login')  # Redirige al usuario a la página de inicio de sesión
    
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a login después del registro exitoso
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})
    
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
     
@api_view(['GET'])
def huella_carbono(request):
    alimento = request.query_params.get('alimento', '').lower()
    if alimento in carbon_footprint_data:
        response = {
            "alimento": alimento,
            "huella_carbono_kg_co2e": carbon_footprint_data[alimento]
        }
    else:
        response = {
            "error": "El alimento especificado no está en la base de datos"
        }
    return Response(response)

def huella(request):
    return render(request, 'huella.html')