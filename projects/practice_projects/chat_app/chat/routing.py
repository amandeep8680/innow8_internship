from django.urls import path
from .consumer import OneToOneChat
from .group_consumer import GroupChatConsumer


websocket_urlpatterns=[
    path("ws/chat/<int:receiver_id>/",OneToOneChat.as_asgi()),
    path("ws/group/<int:room_id>/",GroupChatConsumer.as_asgi()),

  

]