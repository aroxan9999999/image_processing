from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from images.consumers import ImageConsumer

application = ProtocolTypeRouter({
    "http": URLRouter([]),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/images/', ImageConsumer.as_asgi()),
        ])
    ),
})
