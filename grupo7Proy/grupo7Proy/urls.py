from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/usuarios/login/', permanent=False)),
    path('usuarios/', include('usuarios.urls')),
    path('mascotas/', include('mascotas.urls')),
    path('solicitudes/', include('solicitudes.urls')),
    path('historiales/', include('historiales.urls')),
]

# Handler personalizado para 404
def handler404(request, exception):
    from django.shortcuts import render
    return render(request, '404.html', status=404)
