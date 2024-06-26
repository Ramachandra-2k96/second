"""
ASGI config for second project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from chat.consumer import ChatConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second.settings')

ws_patterns=[
    path('ws/chat/',ChatConsumer.as_asgi())
]
application =ProtocolTypeRouter({
    'http':get_asgi_application(),
   'websocket': URLRouter(ws_patterns)
})