from django.urls import path
from . import views

urlpatterns = [
    path('historial/<int:mascota_id>', views.historial_lista, name='historial_lista'),
    path('historialNuevo/<int:mascota_id>', views.historial_nuevo, name='historial_nuevo'),
]
