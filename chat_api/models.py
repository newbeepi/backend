from django.db import models
from django.contrib.auth.models import User


# class Chat(models.Model):
#     participants = models.ManyToManyField(User, related_name='chats')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"chat <{self.id}>"
#
#
# class Message(models.Model):
#     message = models.CharField('message', max_length=400, default='')
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
#     created_at = models.DateTimeField('created_at', auto_now_add=True)


class Message(models.Model):
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def timestamp_value(self):
        return self.timestamp.timestamp()


