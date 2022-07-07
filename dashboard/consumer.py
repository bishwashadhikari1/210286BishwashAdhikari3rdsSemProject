from random import randint
from channels.generic.websocket import WebsocketConsumer
from asyncio import sleep
import json
class GraphConsumer(WebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({'value' : randint(-20, 20)}))
            await sleep(1)