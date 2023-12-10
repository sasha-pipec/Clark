import json

from channels.generic.websocket import AsyncWebsocketConsumer


class MessageWSConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_room = str(self.scope['url_route']['kwargs']['id'])
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_room,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.chat_room,
            {
                **(data | {'type': 'message'})
            }
        )

    async def message(self, event):
        await self.send(text_data=json.dumps({
            **event
        }))
