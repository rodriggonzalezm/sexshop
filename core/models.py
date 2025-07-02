from django.db import models
from cloudinary.models import CloudinaryField

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True, help_text="Código discreto para compras")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = CloudinaryField('imagen', null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

