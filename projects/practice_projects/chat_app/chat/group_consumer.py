from channels.generic.websocket import AsyncWebsocketConsumer
from .services import GroupChatServices
import json


class GroupChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        user = self.scope["user"]

        if user.is_anonymous:
            await self.close()
            return

        self.user = user

    
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]

        
        self.room_group_name = f"room_{self.room_id}"

        # Join roomm
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        history = await GroupChatServices.get_room_history(
            self.room_id
        )


        await self.send(
            text_data=json.dumps({
                "type":"history",
                "messages":history
            },
            default=str)
        )
        print(
            f"{self.user.username} joined room {self.room_id}"
        )



    async def receive(self, text_data):

        data = json.loads(text_data)
    # save message in db
        await GroupChatServices.save_group_message(
            self.room_id,
            self.user,
            data["message"]
        )   
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "group_message",
                "sender": self.user.username,
                "message": data["message"],
                "sender_channel": self.channel_name
            }
        )

    async def group_message(self, event):
        if event["sender_channel"] == self.channel_name:
            return
        await self.send(
            text_data=json.dumps({
                "sender": event["sender"],
                "message": event["message"]
            })
        )




async def disconnect(self,close_code):


    await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )