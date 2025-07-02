import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tripleequis.settings')
django.setup()

from core.models import Producto

def check_images():
    productos = Producto.objects.all()
    for p in productos:
        if p.imagen:
            url = p.imagen.url
            print(f"Producto: {p.nombre} - Imagen URL: {url}")
            if 'res.cloudinary.com' in url:
                print(" --> Imagen en Cloudinary")
            else:
                print(" --> Imagen LOCAL")
        else:
            print(f"Producto: {p.nombre} - SIN imagen")

if __name__ == '__main__':
    check_images()
