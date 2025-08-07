from django.urls import path
from .views import home, catalogo, producto_detalle  # 👈 Importá producto_detalle
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('catalogo/', catalogo, name='catalogo'),
    path("agregar/<str:codigo>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path('eliminar/<str:codigo>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path("api/carrito/", views.api_carrito, name="api_carrito"),
    path("seleccionar_envio/", views.seleccionar_envio, name="seleccionar_envio"),
    path('contacto/', views.contacto, name='contacto'),

    # 🔥 Esta es la línea nueva
    path('producto/<str:codigo>/', views.producto_detalle, name='producto_detalle'),
]
