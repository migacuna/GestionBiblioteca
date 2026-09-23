from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from biblioteca.modelos.libro import Libro
from biblioteca.modelos.usuario import Usuario
from biblioteca.servicios.services import BibliotecaService

def pagina_principal(request):
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'pagina_principal.html', {'libros': libros, 'usuarios': usuarios})

def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        isbn = request.POST['isbn']
        BibliotecaService.agregar_libro(titulo, autor, isbn)
        return redirect('pagina_principal')
    return render(request, 'agregar_libro.html')

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        id_usuario = request.POST['id_usuario']
        BibliotecaService.registrar_usuario(nombre, id_usuario)
        return redirect('pagina_principal')
    return render(request, 'registrar_usuario.html')

def prestar_libro(request, isbn, id_usuario):
    if BibliotecaService.prestar_libro(isbn, id_usuario):
        return redirect('pagina_principal')
    return HttpResponse("No se pudo prestar el libro.")

def devolver_libro(request, isbn):
    if BibliotecaService.devolver_libro(isbn):
        return redirect('pagina_principal')
    return HttpResponse("No se pudo devolver el libro.")

def eliminar_libro(request, isbn):
    if BibliotecaService.eliminar_libro(isbn):
        return redirect('pagina_principal')
    return HttpResponse("No se pudo eliminar el libro.")

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})