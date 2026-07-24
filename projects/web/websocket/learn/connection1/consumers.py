from channels.generic.websocket import AsyncWebsocketConsumer

from .models import *
import json
# testing in the browser

# const socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

# socket.onopen = () => {
#     console.log("Connected");
#     socket.send("Hello Django");
# };

# socket.onmessage = (event) => {
#     console.log("Server:", event.data);
# };
# socket.close();




# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         print("Connection Established")
#         self.accept()

#     # def receive(self,text_data):
#     #     print("Message",text_data)
#     #     self.send(text_data="We recieved your message")













# #     def receive(self, text_data):
# #         print(text_data)
# #         data = json.loads(text_data)
# #         print(data)

# # # socket.onopen = () => {
# # #     socket.send(JSON.stringify({
# # #         message: "Hello",
# # #         sender: 1,
# # #         receiver: 2
# # #     }));
# # # };






# # db me save krna 

#     # def receive(self, text_data):
#     #     data = json.loads(text_data)

#     #     Message.objects.create(
#     #         sender = data['sender'],
#     #         receiver = data['receiver'],
#     #         message = data['message']
#     #     )
#     #     self.send(text_data = "Message Saved")













#     def disconnect(self, close_code):
#         print("Connection Closed")
#         print("Close Code:", close_code)























# user ka Async channel bnanan only 1 use




from channels.db import database_sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        self.group_name = "Hi" 
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
                )
        print("Group:", self.group_name)
        print("Channel:", self.channel_name)
        # print("scope", self.scope)
        await self.accept()

    async def receive(self,text_data):
        data = json.loads(text_data)
        await self.save_message(data)
        await self.send(text_data = "Message Saved")

    @database_sync_to_async
    def save_message(self, data):
        Message.objects.create(
            sender=data["sender"],
            receiver=data["receiver"],
            message=data["message"]
        )
    


    async def disconnect(self,close_code):
        print("connection closed")
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
                )
        self.send("Connection Closed by you",{close_code})


