## Asynchronous Server Gateway Interface
# 1. settings.py
Pehle normal Django me:
WSGI_APPLICATION = "config.wsgi.application"
hota tha.

WebSocket ke liye:
ASGI_APPLICATION = "config.asgi.application"
lagate hain.

Ye kya karta hai?
Django ko batata hai:
"HTTP aur WebSocket requests
asgi.py handle karegi"



# 2. asgi.py

Ye WebSocket project ki sabse important file hai.
- Normal Django me:
Browser
   ↓
urls.py
   ↓
views.py


- WebSocket me:
Browser
   ↓
asgi.py
   ↓
Consumer

- ASGI ka full form:
Asynchronous Server Gateway Interface

- Ye WebSocket samajhta hai.
Normal Django
application = get_asgi_application()

- Sirf HTTP handle karta hai.
Channels ke saath
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(...)
})

Yahan Django bol raha hai:

Agar HTTP request aaye
→ normal Django

Agar websocket aaye
→ websocket route