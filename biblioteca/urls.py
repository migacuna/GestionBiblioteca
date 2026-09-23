from django.contrib import admin
from django.urls import path
from biblioteca.vistas import views

urlpatterns = [
    path('libros', views.libros, name='libros'),
    #path('', views.pagina_principal, name='pagina_principal'),
    #path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    #path('eliminar_libro/<str:isbn>/', views.eliminar_libro, name='eliminar_libro'),
    #path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    #path('prestar_libro/<str:isbn>/<str:id_usuario>/', views.prestar_libro, name='prestar_libro'),
    #path('devolver_libro/<str:isbn>/', views.devolver_libro, name='devolver_libro'),
]
