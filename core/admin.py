from django.contrib import admin
from .models import Producto, ImagenProducto  # <-- importamos ImagenProducto

class ImagenProductoInline(admin.TabularInline):  # o admin.StackedInline si prefieres
    model = ImagenProducto
    extra = 1  # cuántos campos vacíos se muestran por defecto
    max_num = 10  # opcional: máximo de imágenes adicionales

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nombre', 'codigo')
    list_editable = ('disponible',)
    inlines = [ImagenProductoInline]  # <-- aquí agregamos el inline
