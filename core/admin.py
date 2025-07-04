from django.contrib import admin
from .models import Producto, ImagenProducto, Categoria  # <-- importamos ImagenProducto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


class ImagenProductoInline(admin.TabularInline):  # o admin.StackedInline si prefieres
    model = ImagenProducto
    extra = 1  # cuántos campos vacíos se muestran por defecto
    max_num = 10  # opcional: máximo de imágenes adicionales

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'categoria', 'disponible')
    list_editable = ('precio', 'categoria', 'disponible')
    list_filter = ('disponible', 'categoria', 'precio')
    search_fields = ('nombre', 'codigo')
    inlines = [ImagenProductoInline]
