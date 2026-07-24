from channels.generic.websocket import AsyncWebsocketConsumer
from .services import ChatServices
import json
from django.utils import timezone


class OneToOneChat(AsyncWebsocketConsumer):
# toconnect 
    async def connect(self):
        print("Scope:", self.scope["headers"])
        user = self.scope["user"]
        print("user : ",user)
        if user is None or user.is_anonymous:
           await self.close()
           return 
        self.receiver_id  = self.scope["url_route"]["kwargs"]["receiver_id"]

        self.user = user

        self.group_name = f"user_{user.id}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()


        #update status online when user connected 
        await ChatServices.update_online_status(self.user.id,True)

        await self.channel_layer.group_send(
            f"user_{self.receiver_id}",
            {
                "type":"status_update",
                "user":self.user.id,
                "status":True,
                "last_seen":None
            }
        )

        ## get history between two user
        history = await ChatServices.get_history(self.user.id,self.receiver_id
        )

        await self.send(
            text_data=json.dumps({
                "type": "history",
                "messages": history
            }, default=str)
        ) 
        







## receive and send message


    async def receive(self, text_data):
        
        data = json.loads(text_data)

        # save the chat in database
        await ChatServices.savemessage(
            self.user.id, self.receiver_id,data["message"])

        
        # send message to other user
        await self.channel_layer.group_send(
            f"user_{self.receiver_id}",{
                "type":"chat_message",
                "sender":self.user.username,
                "message":data
            }
            
        )  


    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "sender": event["sender"],
            "message": event["message"],
            }))





    async def disconnect(self,close_code):
        await ChatServices.update_online_status(self.user.id,False)
        await ChatServices.update_last_seen(self.user.id)
        await self.channel_layer.group_send(
                f"user_{self.receiver_id}",
                {
                    "type": "status_update",
                    "user": self.user.id,
                    "status": False,
                    "last_seen":str(timezone.now()),
                }
            )
       
        await self.channel_layer.group_discard(
             self.group_name,
             self.channel_name
        )

    async def status_update(self, event):
                await self.send(
                    text_data=json.dumps({
                        "type": "status",
                        "user_id": event["user"],
                        "is_online": event["status"],
                        "last_seen":event["last_seen"]
                    })
                )
     