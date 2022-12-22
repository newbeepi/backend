import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.auth import login
from channels.db import database_sync_to_async


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.scope["session"]["seed"] = random.randint(1, 1000)

        self.user_id = random.randint(1, 100000000)

        # self.user = self.scope["user"]

        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room_group_name = "chat_%s" % self.room_name
        self.group_name = "chat"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.channel_layer.group_send(self.group_name, {"type": "chat_user_id", "user_id": self.user_id})

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        #await login(self.scope, self.user)

        #await database_sync_to_async(self.scope["session"].save)

        data_json = json.loads(text_data)
        message = data_json["message"]

        await self.channel_layer.group_send(self.group_name,
                                            {"type": "chat_message",
                                             "message": message,
                                             "user_id": self.user_id}
        )

    async def chat_message(self, event):
        message = event["message"]
        user_id = event["user_id"]
        await self.send_json(content={"message": message, "userId": user_id})

    async def chat_user_id(self, event):
        await self.send_json(content={"userId": event["user_id"]})
