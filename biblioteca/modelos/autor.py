from django.db import models

class Autor(models.Model):
    id_autor = models.CharField(max_length=10, unique=True)
    nombre = models.TextField(max_length=50)
    nacionalidad = models.TextField(max_length=50)
    
    