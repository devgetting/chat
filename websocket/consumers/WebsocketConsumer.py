from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import json

class WebsocketConsumer(AsyncWebsocketConsumer):
    connected_clients = set()

    async def connect(self):
        await self.accept()

        self.connected_clients.add(self)

    async def disconnect(self, code):
        return await super().disconnect(code)

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response = {
            'message': f'Mensaje: %s' % (message)
        }

        await self.broadcast_message(json.dumps(response))

    @classmethod
    async def broadcast_message(cls, message):
        await asyncio.gather(
            *(client.send_message(message) for client in cls.connected_clients )
        )

    async def send_message(self, message):
        await self.send(text_data=message)