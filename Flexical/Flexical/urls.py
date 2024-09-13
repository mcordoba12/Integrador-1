"""
URL configuration for Flexical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FlexicalApp.urls')),  # Incluye las URLs de FlexicalApp
    path('', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación de Django
    path('', include('register.urls')),  # Incluye las URLs de la aplicación 'register'
    path('', include('login.urls')),  # Incluye las URLs de la aplicación 'login'
]

urlpatterns += staticfiles_urlpatterns()

