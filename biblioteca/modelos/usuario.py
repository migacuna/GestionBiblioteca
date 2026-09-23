from django.db import models

class Usuario(models.Model):
    nombre = models.TextField(max_length=50)
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField(default=True)
    id_usuario = models.CharField(max_length=10, unique=True)

    def estadoUsuario(self):
        if self.estado:
            self.estado = True
        else:
            self.estado = False    
        self.save()  
