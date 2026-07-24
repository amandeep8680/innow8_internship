from django.urls import path
from .consumers import *
print("WEBSOCKET ROUTING LOADED")

websocket_urlpatterns=[
    path("ws/chat/<int:receiver_id>/",ChatConsumer.as_asgi())
]