import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class TaskConsumer(WebsocketConsumer):
    def connect(self):
        # TODO Allow Multiple instances the app to run on the same server
        self.room_group_name = 'tasks'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name)

    def receive(self, text_data):
        data_json = json.loads(text_data)
        message_type = data_json['message_type']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'send_message_type',
                'message_type': message_type
            }
        )

    def send_message_type(self, event):
        self.send(json.dumps(
            {
                'message_type': event['message_type']
            }
        ))
