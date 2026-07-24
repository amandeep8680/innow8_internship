from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    mobile = models.IntegerField(null= True)
    is_online = models.BooleanField(default = False)
    last_seen = models.DateTimeField(null = True , blank = True)

    def __str__(self):
        return self.username
    


class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE , related_name="sent_message")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE , related_name="receive_message")
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
