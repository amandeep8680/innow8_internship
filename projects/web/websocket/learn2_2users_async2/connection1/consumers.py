

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import *
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope.get("user")
        print("User:", user)
        print("Anonymous:", user.is_anonymous if user else None)
        if user is None or user.is_anonymous:
            await self.close(code=4001)
            return

        self.user = user
        
        receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]

        self.group_name = f"user_{self.user.id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        print("Joined",self.group_name)
        await self.accept()


        # online status
        await self.update_online_status(True)





    


        # History 
        history = await self.get_message(
            self.user.id,receiver_id
        )

        await self.send(
            text_data = json.dumps({
                "type":"history",
                "message":history
            },default = str)
        )
       

# sending user the next perason ins online or ofline
      


        await self.update_online_status(True)

        await self.channel_layer.group_send(
            f"user_{receiver_id}",
            {
                "type": "status_update",
                "user_id": self.user.id,
                "is_online": True,
                "last_seen": None,
            }
        )

        
       








    async def receive(self, text_data):
        
        data = json.loads(text_data)
        sender = self.user
        receiver = self.scope["url_route"]["kwargs"]["receiver_id"]      
        message = data["message"]


        # save in db
        await self.save_message( receiver, message
        )


        # send to the receiver
        await self.channel_layer.group_send(
            f"user_{receiver}",
            {
                "type":"chat_message",
                "sender" : self.user.id,
                "message" : message
                
            }
        )
        









    async def disconnect(self, close_code):
        receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]
        await self.update_online_status(False)
        await self.update_last_seen()
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            f"user_{receiver_id}",
            {
                "type": "status_update",
                "user_id": self.user.id,
                "is_online": False,
                "last_seen": str(timezone.now()),
            }
        )










    async def chat_message(self,event):

   

        await self.send(
            text_data = json.dumps({
                "sender" : event["sender"],
                "message" :event["message"]


            })
            )
        
   
           
        
    @database_sync_to_async
    def save_message(self ,receiver , message):
        sender_user = self.user
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
    

















    @database_sync_to_async
    def update_online_status(self, status):
        self.user.is_online = status
        self.user.save()


    @database_sync_to_async
    def update_last_seen(self):
        self.user.last_seen = timezone.now()
        self.user.save()



    @database_sync_to_async
    def get_status(self , receiver_id):
        this_user = User.objects.get(id=receiver_id)
        return {
            "is_online": this_user.is_online,
            "last_seen": this_user.last_seen,
        }

    async def status_update(self, event):
        await self.send(
            text_data=json.dumps({
                "type": "status",
                "user_id": event["user_id"],
                "is_online": event["is_online"],
                "last_seen": event["last_seen"],
            })
        )