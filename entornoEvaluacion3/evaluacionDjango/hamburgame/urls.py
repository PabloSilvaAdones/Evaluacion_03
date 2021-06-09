from django.urls import path
from .views import inicio, normales, premium, listarTipo, crearTipo,  modificarTipo, eliminarTipo

urlpatterns = [
    path('', inicio, name="inicio"),
    path('normales', normales, name="normales"),
    path('premium', premium, name="premium"),






    path('listarTipo', listarTipo, name="listarTipo"),
    path('crearTipo', crearTipo, name="crearTipo"),
    path('modificarTipo/<id>', modificarTipo, name="modificarTipo"),
    path('eliminarTipo/<id>', eliminarTipo, name="eliminarTipo"),
]