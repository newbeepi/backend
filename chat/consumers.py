import json
import random

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.renderers import JSONRenderer

from chat_api.serializers import MessageSerializer
from operations_with_db import save_message, get_chat_history


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.scope["session"]["seed"] = random.randint(1, 1000)

        self.channel_layer.send(self.channel_name, {"history": get_chat_history()})
        self.group_name = "chat"
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json["message"]
        username = data_json["username"]
        await save_message(message=message, username=username)
        await self.channel_layer.group_send(self.group_name,
                                            {"type": "chat_message",
                                             "message": message,
                                             "username": username
                                             }
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send_json(content={"message": {"message": message, "username": username}})

    async def chat_history(self, event):
        history = event["history"]
        serializer = MessageSerializer(history)
        json_history = JSONRenderer().render({"history": serializer.data})
        await self.send(text_data=json_history)
