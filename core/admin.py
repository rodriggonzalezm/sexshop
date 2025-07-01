from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'disponible')  # columnas visibles en la lista
    list_filter = ('disponible',)  # filtros en la barra lateral
    search_fields = ('nombre', 'codigo')  # búsqueda rápida por nombre o código
    list_editable = ('disponible',)  # permite editar este campo desde la lista
