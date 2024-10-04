from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('ventas',venta, name="venta"),
    path('formulario',formu, name="formu"),
    path('logout', logout, name="logout"),
    path('recomendaciones', recom, name="recom"),
    path('registro', registro, name="registro"),
    path('carrito', carrito, name="carrito"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('limpiar', limpiar),
    path('comprar', comprar, name="comprar"),
    path('login', LoginView.as_view(template_name='login.html'),name="login"),
]
