from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('images', self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('images', self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'message': data
        }))

    async def image_processed(self, event):
        image_id = event['image_id']
        await self.send(text_data=json.dumps({
            'message': f'Image {image_id} has been processed and uploaded.'
        }))
