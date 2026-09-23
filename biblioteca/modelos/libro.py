from django.db import models
from biblioteca.modelos.autor import Autor

class Libro(models.Model):
    ##titulo = models.CharField(max_length=100)
    ##autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.save()
            return True
        return False

    def devolver(self):
        self.disponible = True
        self.save()
