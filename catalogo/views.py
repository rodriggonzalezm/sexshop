from django.shortcuts import render
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/index.html', {
        'productos': productos,
        'meta_title': 'Sexshop en Concepción - Envíos Discretos a Todo Chile',
        'meta_description': 'Catálogo íntimo con despacho confidencial en Chile. Atención desde Concepción a todo el país.'
    })
