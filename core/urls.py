from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth.views import LoginView
from .views import analyze_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('inicio',inicio, name="inicio"),
    path('nosotros',nosotros, name="nosotros"),
    path('logout', logout, name="logout"),
    path('proyectos', proyectos, name="proyectos"),
    path('registro', registro, name="registro"),
    path('contactos', contactos, name="contactos"),
    path('login', LoginView.as_view(template_name='login.html'),name="login"),
    path('analyze/', analyze_recipe, name='analyze_recipe'),
]
