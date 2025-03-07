from django.db import models

# Create your models here.
from django.db import models

class Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=50, unique=True)
    mac_address = models.CharField(max_length=17, unique=True)
    estado = models.CharField(max_length=20, choices=[('Listo', 'Listo'), ('En prueba', 'En prueba')])
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.modelo} - {self.numero_serie}"


