import json
from .models import OneToOneChat ,ChatRoom, RoomMember ,GroupMessage
from .serializers import OneToOneChatSerializer
from channels.db import database_sync_to_async
from authentication.models import User  
from django.utils import timezone


 

class ChatServices:

    @staticmethod
    def get_users(request):
        user=request.user

        user = User.objects.exclude(id=user.id).values(
            "id",
            "username",
            "is_online",
            "last_seen"
        )
        return list(user)

    @staticmethod
    def get_group(request):

        user = request.user


        groups = ChatRoom.objects.filter(
            members__user=user
        ).values(
            "id",
            "name",
            "created_by__username",
            "created_at"
        )


        return list(groups)

    @staticmethod
    @database_sync_to_async
    def get_history(user , receiver):
        message=OneToOneChat.objects.filter(
            user__in=[user,receiver],
            receiver__in = [receiver, user]
        ).order_by("created_at")[:50]

        return list(
            message.values(
                "user_id","receiver_id","message","created_at"
            )
        )


    @staticmethod
    @database_sync_to_async
    def savemessage(user,receiver,message):
        user=User.objects.get(id=user)
        receiver=User.objects.get(id=receiver)
        return OneToOneChat.objects.create(
                user=user,
                receiver=receiver,
                message=message
            )





    ## update on_online status off receiver
    @staticmethod
    @database_sync_to_async
    def update_online_status(user,status):
        user=User.objects.get(id=user)
        user.is_online=status
        user.save(update_fields=["is_online"])


    ## update last_seen
    @staticmethod
    @database_sync_to_async
    def update_last_seen(user):
        user=User.objects.get(id=user)
        user.last_seen = timezone.now()
        user.save(update_fields=["last_seen"])







    #### Group Services 
class GroupChatServices:
## to create the room 
    @staticmethod
    def create_room(user, name, members):

        room = ChatRoom.objects.create(
            name=name,
            created_by=user
        )

        RoomMember.objects.create(
            room=room,
            user=user
        )

        for user_id in members:
            if user_id == user.id:
                continue

            member = User.objects.get(id=user_id)

            RoomMember.objects.create(
                room=room,
                user=member
            )

        return room.id

## Saving message in the group
    @staticmethod
    @database_sync_to_async
    def save_group_message(room_id, user, message):

        return GroupMessage.objects.create(
            room_id=room_id,
            sender=user,
            message=message
        )

## Fetching hiostiory of chat
    @staticmethod
    @database_sync_to_async
    def get_room_history(room_id):

        messages = GroupMessage.objects.filter(
            room_id=room_id
        ).select_related(
            "sender"
        ).order_by(
            "created_at"
        )


        return list(
            messages.values(
                "sender__username",
                "message",
                "created_at"
            )
        )