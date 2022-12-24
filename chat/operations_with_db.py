from asgiref.sync import sync_to_async
from django.utils import timezone
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from chat_api.models import Message
from chat_api.serializers import MessageSerializer

import io

@sync_to_async()
def save_message(username, message):
    message = Message(username=username, message=message)
    message.save()


@sync_to_async()
def get_chat_history():
    history = Message.objects.filter(timestamp__lte=timezone.now()).order_by('-timestamp')[:20]
    serializer = MessageSerializer(history, many=True)
    json_history = JSONRenderer().render({"history": serializer.data})
    return json_history
