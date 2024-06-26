# images/tests/test_websocket.py
from channels.testing import WebsocketCommunicator
from django.test import TransactionTestCase
from image_processing_api.routing import application

class WebSocketTests(TransactionTestCase):
    async def test_websocket_connection(self):
        communicator = WebsocketCommunicator(application, "/ws/images/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.disconnect()
