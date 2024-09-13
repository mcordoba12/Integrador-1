from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registerPFrelancer/', views.registerPFrelancer, name='registerPFrelancer'),
    path('registerClient/', views.register_client, name='register_client'),
]
