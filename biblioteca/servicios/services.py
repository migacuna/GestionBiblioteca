from biblioteca.modelos import Libro, Usuario

class BibliotecaService:
    @staticmethod
    def agregar_libro(titulo, autor, isbn):
        libro = Libro(titulo=titulo, autor=autor, isbn=isbn)
        libro.save()
        return libro

    @staticmethod
    def eliminar_libro(isbn):
        libro = Libro.objects.filter(isbn=isbn).first()
        if libro:
            libro.delete()
            return True
        return False

    @staticmethod
    def registrar_usuario(nombre, id_usuario):
        usuario = Usuario(nombre=nombre, id_usuario=id_usuario)
        usuario.save()
        return usuario

    @staticmethod
    def prestar_libro(isbn, id_usuario):
        libro = Libro.objects.filter(isbn=isbn, disponible=True).first()
        usuario = Usuario.objects.filter(id_usuario=id_usuario).first()
        if libro and usuario:
            libro.prestar()
            return True
        return False

    @staticmethod
    def devolver_libro(isbn):
        libro = Libro.objects.filter(isbn=isbn).first()
        if libro:
            libro.devolver()
            return True
        return False
