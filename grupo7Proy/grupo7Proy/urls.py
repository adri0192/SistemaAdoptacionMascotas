"""
URL configuration for grupo7Proy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/mascotas/', permanent=False)),
    path('usuarios/', include('usuarios.urls')),
    path('mascotas/', include('mascotas.urls')),
    path('solicitudes/', include('solicitudes.urls')),
    path('historiales/', include('historiales.urls')),
]

# Handler personalizado para 404
def handler404(request, exception):
    from django.shortcuts import render
    return render(request, '404.html', status=404)

