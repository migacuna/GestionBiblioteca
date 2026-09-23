from datetime import datetime
from django.db import models

from gestion_biblioteca.biblioteca.modelos.libro import Libro
from gestion_biblioteca.biblioteca.modelos.usuario import Usuario

class PrestaLibro(models.Model):
    usuario_id = models.ForeignKey(Usuario, unique=True)
    Libro = models.ForeignKey(Libro)
    fechaPrestamo = models.DateField
    fechaEntrega = models.DateField
    estado = models.BooleanField(default=True)
    
    def validaPrestamo(self):
        hoy = datetime.date()
        if hoy > self.fechaEntrega:
            self.estado = False
            self.save()
            
        