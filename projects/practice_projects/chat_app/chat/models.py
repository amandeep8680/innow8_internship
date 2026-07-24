from django.db import models
from django.conf import settings

# Create your models here.
class OneToOneChat(models.Model):
    '''model to send chat between one to one user '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="receiver")
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} -> {self.receiver}"






## group chat 

class ChatRoom(models.Model):
    '''create the room and add the member's'''
    name = models.CharField(max_length=100,blank=True,null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="created_rooms")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"Room {self.id}"


class RoomMember(models.Model):
    '''Memebers of the group for fusther interact with '''
    room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name="members")

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="room_memberships")

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("room", "user")

    def __str__(self):
        return f"{self.user.username} - {self.room.id}"





class GroupMessage(models.Model):

    room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name="messages")

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.sender.username}: {self.message}"