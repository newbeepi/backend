from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # path('chats/', views.ChatList.as_view()),
    # path('chats/<int:pk>/', views.ChatDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('messages/', views.MessageCreate.as_view()),
    path('messages/', views.MessageDetail.as_view()),
    path('messages/getHistory/', views.MessageGetHistory.as_view()),
    path('messages/getUpdates/', views.MessageGetUpdates.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
