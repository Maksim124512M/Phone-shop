"""
WSGI config for mobile_shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application


path = '/home/Maksym201/Phone-shop'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobile_shop.settings')

application = get_wsgi_application()
