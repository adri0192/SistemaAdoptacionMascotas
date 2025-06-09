from django.urls import path
from . import views

app_name = 'historiales'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('agregar/', views.agregar, name='agregar'),
    path('cargar-mascotas-por-especie/', views.cargar_mascotas_por_especie, name='cargar_mascotas_por_especie'),
]
