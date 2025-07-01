import os
from os import path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tripleequis.settings')

application = get_wsgi_application()
static_root = path.join(path.dirname(__file__), 'staticfiles')
application = WhiteNoise(application, root=static_root)
