from django.urls import path
from . import views

urlpatterns = [
    path('mascota/<int:mascota_id>/historial/', views.historial_lista, name='historial_lista'),
    path('mascota/<int:mascota_id>/historial/nuevo/', views.historial_nuevo, name='historial_nuevo'),
]
