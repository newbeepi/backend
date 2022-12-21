
from rest_framework import serializers

# from django.contrib.auth.models import User

from .models import Message


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#
#
# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ['message', 'user', 'chat']
#
#     def to_representation(self, instance):
#         user = instance.user
#         return {
#             "user_id": user.id,
#             "username": user.username,
#             "message_id": instance.id,
#             "message":instance.message,
#             'sent': instance.created_at
#         }
#
#     def create(self, validated_data):
#         chat = validated_data.pop('chat')
#         user = validated_data.pop('user')
#         message = Message.objects.create(user=user, chat=chat, **validated_data)
#         return message
#
# # class MessagesDataField(serializers.SlugRelatedField):
# #     def to_representation(self, obj):
# #         user = obj.user.username
# #         return {user: obj.message, 'sent': obj.created_at}
#
#
# class ChatSerializer(serializers.ModelSerializer):
#     participants = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='username'
#     )
#     # participants = ChatHyperlink(
#     #     many=True,
#     # )
#     messages = MessageSerializer(many=True)
#
#     class Meta:
#         model = Chat
#         fields = ['id', 'participants', 'messages']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'timestamp']
