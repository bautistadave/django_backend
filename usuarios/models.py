from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)   