import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StockUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'stock_updates'

        # Join the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        stock_data = text_data_json['stock_data']

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'stock_update',
                'stock_data': stock_data
            }
        )

    # Receive message from group
    async def stock_update(self, event):
        stock_data = event['stock_data']

        # Send stock update to WebSocket
        await self.send(text_data=json.dumps({
            'stock_data': stock_data
        }))
