from django.contrib import admin

from .models import Message #, Chat


class MessageInline(admin.TabularInline):
    model = Message
    readonly_fields = ('message', 'timestamp', )
    extra = 0
    can_delete = False
    ordering = ('timestamp', )
#
#
# class ChatAdmin(admin.ModelAdmin):
#     model = Chat
#     inlines = (MessageInline, )
#     readonly_fields = ('participants', )


admin.site.register(Message)