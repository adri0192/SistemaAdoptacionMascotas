from django.urls import path
from . import views

app_name = 'mascotas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:mascota_id>/', views.detalle, name='detalle'),
    path('gestionar/', views.gestionar, name='gestionar'),
    path('agregar/', views.agregar, name='agregar'),
    path('editar/<int:mascota_id>/', views.editar,  name='editar'),
    path('eliminar/<int:mascota_id>/', views.eliminar, name='eliminar'),
]
