import os
import django
from cloudinary.uploader import upload

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tripleequis.settings')
django.setup()

from core.models import Producto

def upload_local_images():
    productos = Producto.objects.all()
    for p in productos:
        if p.imagen:
            url = p.imagen.url
            if 'res.cloudinary.com' not in url:
                print(f"Subiendo imagen local del producto: {p.nombre}")
                path_local = p.imagen.path
                if os.path.exists(path_local):
                    try:
                        with open(path_local, 'rb') as f:
                            res = upload(f, public_id=f"productos/{os.path.basename(path_local)}", overwrite=True)
                            # Cloudinary devuelve la url segura
                            p.imagen = res['secure_url']
                            p.save()
                            print(f"Imagen subida y actualizada para {p.nombre}")
                    except Exception as e:
                        print(f"Error al subir imagen de {p.nombre}: {e}")
                else:
                    print(f"No se encontró archivo local para {p.nombre} en {path_local}")
            else:
                print(f"Producto {p.nombre} ya tiene imagen en Cloudinary")
        else:
            print(f"Producto {p.nombre} no tiene imagen")

if __name__ == '__main__':
    upload_local_images()
