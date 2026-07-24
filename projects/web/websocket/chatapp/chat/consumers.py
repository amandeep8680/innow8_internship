import json 
from channels.generic.websocket import WebsocketConsumer



# user1 - user1 
# class ChatCustomer(WebsocketConsumer):

#     def connect(self):
#         print('Client Connected')

#         self.accept()

#         self.send(
#             text_data=json.dumps({
#                 "message":"Connected Succeffsully"
#             })
#         )

#     def receive(self,text_data):
#         print("Recieved : ",text_data)
        
#         data = json.loads(text_data)

#         message = data.get("message")

#         self.send(text_data=json.dumps({
#             "message":message 
#         }))

#     def disconnect(self, close_code):
#         print("Client Disconnected")






from asgiref.sync import async_to_sync

class ChatCustomer(WebsocketConsumer):
    
    def connect(self):
        self.room_name=f"chat_{self.scope['url_route']['kwargs']['room_id']}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.accept()


    def receive(self,text_data):
        data = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_name,{
                "type":"chat_message",
                "message":data["message"]
            }
        )
        
    def chat_message(self, event):
        print("CHAT MESSAGE CALLED")
        self.send(text_data=json.dumps({
            "message": event["message"]
        }))
