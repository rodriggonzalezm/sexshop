from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Producto, ImagenProducto, Categoria



def home(request):
    envio = request.session.get("envio", "concepcion")
    total_carrito = sum(item["cantidad"] for item in request.session.get("carrito", {}).values())
    return render(request, 'core/home.html', {
        'envio': envio,
        'total_carrito': total_carrito,
    })

def producto_detalle(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo, disponible=True)
    imagenes_adicionales = ImagenProducto.objects.filter(producto=producto)
    
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.producto = producto
            resena.save()
            messages.success(request, '¡Gracias por tu reseña!')
            return redirect('producto_detalle', codigo=codigo)
    else:
        form = ResenaForm()

    carrito = request.session.get("carrito", {})
    total_carrito = sum(item["cantidad"] for item in carrito.values())

    contexto = {
        'producto': producto,
        'imagenes_adicionales': imagenes_adicionales,
        'total_carrito': total_carrito,
        'form': form,
    }
    return render(request, 'core/producto_detalle.html', contexto)

def agregar_resena(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.producto = producto
            resena.save()
            messages.success(request, '¡Gracias por tu reseña!')
            return redirect('producto_detalle', codigo=producto.codigo)
    
    return redirect('producto_detalle', codigo=producto.codigo)


def catalogo(request):
    categoria_id = request.GET.get("categoria")
    productos = Producto.objects.filter(disponible=True)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    categorias = Categoria.objects.all()

    carrito = request.session.get("carrito", {})
    total_carrito = sum(item["cantidad"] for item in carrito.values())

    envio = request.session.get("envio", "concepcion")
    costos_envio = {"concepcion": 3990, "region": 5990}
    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito.values())
    costo_envio = costos_envio.get(envio, 3990)
    total = subtotal + costo_envio

    contexto = {
        'productos': productos,
        'categorias': categorias,
        'categoria_activa': int(categoria_id) if categoria_id else None,
        'total_carrito': total_carrito,
        'subtotal': subtotal,
        'costo_envio': costo_envio,
        'total': total,
        'carrito': carrito,
        'envio': envio,
    }
    return render(request, 'core/catalogo.html', contexto)



def agregar_al_carrito(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    carrito = request.session.get('carrito', {})

    if codigo in carrito:
        carrito[codigo]['cantidad'] += 1
    else:
        carrito[codigo] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1,
            'imagen_url': producto.imagen.url if producto.imagen else '',
        }

    request.session['carrito'] = carrito
    request.session.modified = True
    messages.success(request, f'Se agregó "{producto.nombre}" al carrito correctamente.')
    return redirect('catalogo')


def eliminar_del_carrito(request, codigo):
    carrito = request.session.get('carrito', {})
    if codigo in carrito:
        del carrito[codigo]
        request.session['carrito'] = carrito
        request.session.modified = True
        messages.success(request, f'Producto eliminado del carrito.')
    return redirect('catalogo')


def seleccionar_envio(request):
    envio = request.GET.get("envio", "concepcion")
    if envio not in ["concepcion", "region"]:
        envio = "concepcion"
    request.session["envio"] = envio
    return JsonResponse({"envio": envio})


def api_carrito(request):
    carrito = request.session.get("carrito", {})
    envio = request.session.get("envio", "concepcion")
    costos_envio = {"concepcion": 3990, "region": 5990}

    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito.values())
    costo_envio = costos_envio.get(envio, 3990)
    total = subtotal + costo_envio

    productos = []
    for codigo, item in carrito.items():
        productos.append({
            "codigo": codigo,
            "nombre": item["nombre"],
            "precio": item["precio"],
            "cantidad": item["cantidad"],
        })

    return JsonResponse({
        "productos": productos,
        "subtotal": subtotal,
        "costo_envio": costo_envio,
        "total": total,
        "envio": envio,
    })

def contacto(request):
    return render(request, 'core/contacto.html')
