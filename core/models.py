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

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    imagen = CloudinaryField('imagen')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"