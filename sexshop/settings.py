# Django settings (simplificado para ejemplo)
SECRET_KEY = 'django-insecure-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['django.contrib.staticfiles', 'catalogo']
ROOT_URLCONF = 'sexshop.urls'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
    ]},
}]
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}
