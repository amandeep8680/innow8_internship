print("ROUTING FILE LOADED") 
from django.urls import re_path
from .consumers import ChatCustomer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_id>\w+)/$", ChatCustomer.as_asgi()),
]               