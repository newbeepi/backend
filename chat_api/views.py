from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

import datetime

from chat_api.models import Message  # Chat
from chat_api.serializers import MessageSerializer  # , ChatSerializer, UserSerializer


#
# class ChatList(generics.ListCreateAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer
#
#
# class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


# class MessageCreate(APIView):
#     def post(self, request, format=None):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetail(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageGetMessages(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        if 'timestamp' in request.data.keys():
            timestamp = datetime.datetime.fromtimestamp(int(request.data['timestamp']))
        else:
            timestamp = datetime.datetime.now()
        queryset = self.get_queryset()
        serializer = MessageSerializer(queryset.filter(timestamp__lte=timestamp).order_by('-timestamp')[:20],
                                       many=True)

        return Response(serializer.data)


# class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
