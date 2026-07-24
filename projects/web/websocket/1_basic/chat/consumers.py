from channels.generic.websocket import AsyncWebsocketConsumer # type: ignore
import json

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("CONNECTED")
        await self.accept()

    async def receive(self, text_data):
        print("MESSAGE RECEIVED:", text_data)

        await self.send(
            text_data=json.dumps({
                "message": "Server received: " + text_data
            })
        )