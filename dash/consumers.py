from cgitb import text
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class GraphConsumer(WebsocketConsumer):
    def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = 'chat_%s' % self.room_name
        self.group_name = self.scope['url_route']['kwargs']['groupkoname']

        # async_to_sync(self.channel_layer.group_add)(
        #     self.group_name,
        #     self.channel_name
        # )
        print(self.group_name)
        self.accept()
        print("#######CONNECTED############")

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.channel_name, 'render_updates_group')
        print("DISCONNECED CODE: ", close_code)

    def receive(self, text_data=None, bytes_data=None):
        print(" MESSAGE RECEIVED")
        data = json.loads(text_data)
        message = data['message']
        self.send(text_data=data)

    # def send_message_to_frontend(self,event):
    #     print("EVENT TRIGERED")
    #     # Receive message from room group
    #     message = event['message']
    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))