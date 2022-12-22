import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.auth import login
from channels.db import database_sync_to_async


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.scope["session"]["seed"] = random.randint(1, 1000)

        self.group_name = "chat"
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json["message"]
        username = data_json["username"]
        await self.channel_layer.group_send(self.group_name,
                                            {"type": "chat_message",
                                             "message": message,
                                             "username": username}
        )


    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send_json(content={"message": message, "username": username})
