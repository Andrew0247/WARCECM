"""
WSGI config for RegContrac project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append("C:/Users/57323/Desktop/Practica/ProyectoDjango/RegContrac")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RegContrac.settings')

application = get_wsgi_application()
