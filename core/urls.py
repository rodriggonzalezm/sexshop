from django.urls import path
from .views import home, catalogo, producto_detalle  # 👈 Importá producto_detalle
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<str:codigo>/', views.producto_detalle, name='producto_detalle'),
    path('agregar-al-carrito/<str:codigo>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<str:codigo>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('seleccionar-envio/', views.seleccionar_envio, name='seleccionar_envio'),
    path('api/carrito/', views.api_carrito, name='api_carrito'),
    path('contacto/', views.contacto, name='contacto'),
    path('producto/<int:producto_id>/agregar-resena/', views.agregar_resena, name='agregar_resena'),
]