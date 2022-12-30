# Structures
## Message:
```
chatId: number                          (chat id)
id: number                              (message id in chat)
authorId: number                        (id of user who submitted message)
timestamp: unix-timestamp-ms            (time when message was saved at server)
text: string                            (message text encoded in utf-8)
```
## User:
```
id: number                              (user id)
username: string                        (user name)
```
## Chat:
```
id: number                              (chat id)
name: string                            (name of chat)
```
## Action: (backend side exclusive)
```
chatId: number                          (chat id)
actionId: number                        (action id)
type: enum || string                    (enum or string that specifies action type)
details: type-specific-data             (action data according to type)
```
# Methods
## Chat:
```
queryHistory:
     -> chatId: number
        from: null || number            (N messages before message with id or newest N messages)
     <- messages: Message[]             (N messages returned from server)
```
```
queryUpdates:
     -> chatId: number
        fromMessage: number             (message id)
        toMessage: number               (message id)
        timestamp: unix-timestamp-ms    (updates after timestamp)
     <- messages: Message[]             (updated messages that changed since timestamp)
```
```
sendMessage:
     <- chatId: number
        text: string 
     -> message: Message
```
```
queryMembers:
     <- chatId: number                  (chat id)
     -> users: number[]                 (array of user id's that belong to chat)
```
```
updateMessage:
     <- chatId: number                  (chat id)
        messageId: number
        text: string
     -> users: number[]                 (array of user id's that belong to chat)
```
## User:
```
queryUsers:
     <- userIds: number[]               (user id's to querry info about)
     -> users: User[]                   (user data's returned from server)
```
