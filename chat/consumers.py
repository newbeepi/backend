import json
import random
import logging

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .operations_with_db import save_message, get_chat_history

logger = logging.getLogger(__name__
                           )


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        logger.info("Attempting to connect to WSS")
        self.scope["session"]["seed"] = random.randint(1, 1000)

        logger.info("Adding chanel to group")
        self.group_name = "chat"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        logger.info("Added")

        logger.info("Trying to accept connection")
        await self.accept()
        logger.info("Connected")

        logger.info("Getting messages history")
        history = await get_chat_history()
        logger.info("Success")

        logger.info("Sending chat history")
        await self.channel_layer.send(self.channel_name, {"type": "chat_history", "history": history})
        logger.info("Sent")

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        logger.info("Receiving message")
        data_json = json.loads(text_data)
        logger.info("Received")
        message = data_json["message"]
        username = data_json["username"]
        logger.info("Saving message")
        await save_message(message=message, username=username)
        logger.info("Saved")
        logger.info("Sending message to group")
        await self.channel_layer.group_send(self.group_name,
                                            {"type": "chat_message",
                                             "message": message,
                                             "username": username
                                             }
                                            )
        logger.info("Sent")

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send_json(content={"message": {"message": message, "username": username}})

    async def chat_history(self, event):
        json_history = event["history"]
        await self.send_json(content=json_history)
