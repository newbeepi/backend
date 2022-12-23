from asgiref.sync import sync_to_async

from chat_api.models import Message


@sync_to_async
def save_message(username, message):
    message = Message(username=username, message=message)
    message.save()
