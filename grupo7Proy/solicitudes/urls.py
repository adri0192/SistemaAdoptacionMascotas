from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('solicitar/<int:mascota_id>/', views.solicitar, name='solicitar'),
    path('mis-solicitudes/', views.mis_solicitudes, name='mis_solicitudes'),
    path('gestionar/', views.gestionar, name='gestionar'),
    path('procesar/<int:solicitud_id>/<str:accion>/', views.procesar, name='procesar'),
]
