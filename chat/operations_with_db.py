from asgiref.sync import sync_to_async
from django.utils import timezone

from chat_api.models import Message


@sync_to_async()
def save_message(username, message):
    message = Message(username=username, message=message)
    message.save()
    return message.timestamp


@sync_to_async()
def get_chat_history():
    return Message.objects.filter(timestamp__lte=timezone.now()).order_by('-timestamp')[:20]