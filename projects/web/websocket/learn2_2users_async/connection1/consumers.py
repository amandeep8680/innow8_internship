from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import *


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope["url_route"]["kwargs"]["user_id"]
        receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]

        self.group_name = f"user_{user_id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        print("Joined",self.group_name)
        await self.accept()


        # History 
        history = await self.get_message(
            user_id,receiver_id
        )

        await self.send(
            text_data = json.dumps({
                "type":"history",
                "message":history
            },default = str)
        )






















    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = self.scope["url_route"]["kwargs"]["user_id"]
        receiver = self.scope["url_route"]["kwargs"]["receiver_id"]      
        message = data["message"]


        # save in db
        await self.save_message(
            sender, receiver, message
        )


        # send to the receiver
        await self.channel_layer.group_send(
            f"user_{receiver}",
            {
                "type":"chat_message",
                "sender" : sender,
                "message" : message
                
            }
        )
        



    async def chat_message(self,event):

        print(event)

        await self.send(
            text_data = json.dumps({
                "sender" : event["sender"],
                "message" :event["message"]


            })
            )
        
   
           
        
    @database_sync_to_async
    def save_message(self , sender , receiver , message):
        sender_user = User.objects.get(id = sender)
        receiver_user = User.objects.get(id = receiver)
        Message.objects.create(
            sender = sender_user ,
            receiver = receiver_user,
            message = message
        )
    

    @database_sync_to_async
    def get_message(self, user1,user2):
        messages = Message.objects.filter(
            sender__in = [user1,user2],
            receiver__in = [user1,user2]
        ).order_by("created_at")

        return list(messages.values(
            "sender_id","receiver_id","message","created_at"
        ))        
    