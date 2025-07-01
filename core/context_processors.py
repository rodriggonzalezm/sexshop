def carrito(request):
    carrito = request.session.get("carrito", {})
    total_carrito = sum(item["cantidad"] for item in carrito.values())
    return {
        'carrito': carrito,
        'total_carrito': total_carrito,
    }

def carrito_y_envio(request):
    carrito = request.session.get("carrito", {})
    total_carrito = sum(item["cantidad"] for item in carrito.values())

    envio = request.session.get("envio", "concepcion")
    costos_envio = {"concepcion": 3990, "region": 5990}
    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito.values())
    costo_envio = costos_envio.get(envio, 3990)
    total = subtotal + costo_envio

    return {
        "carrito": carrito,
        "total_carrito": total_carrito,
        "subtotal": subtotal,
        "costo_envio": costo_envio,
        "total": total,
        "envio": envio,
    }