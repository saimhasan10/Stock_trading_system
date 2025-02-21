import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StockUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "stock_updates"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        stock_symbol = data['stock_symbol']
        price = data['price']

        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'stock_update',
                'stock_symbol': stock_symbol,
                'price': price
            }
        )

    async def stock_update(self, event):
        await self.send(text_data=json.dumps({
            'stock_symbol': event['stock_symbol'],
            'price': event['price']
        }))
